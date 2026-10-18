"""Run owned-code state-modification and signed-license learning fixtures on Linux x86-64."""

import ctypes
import hashlib
import json
import platform
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import capstone
import lief
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey


class Player(ctypes.Structure):
    _fields_ = [("health", ctypes.c_int32), ("score", ctypes.c_int32)]


def game_lab(root):
    compiler = shutil.which("gcc")
    if compiler is None:
        raise RuntimeError("gcc is required for this owned-code exercise")
    source = root / "labs/game_state.c"
    with tempfile.TemporaryDirectory(prefix="reversing-owned-lab-") as temporary:
        library_path = Path(temporary) / "game_state.so"
        subprocess.run(
            [compiler, "-shared", "-fPIC", "-O0", "-g", "-Wall", "-Wextra", "-Werror",
             str(source), "-o", str(library_path)],
            check=True, capture_output=True, timeout=30,
        )
        binary = lief.parse(str(library_path))
        symbol = next(item for item in binary.symbols if item.name == "apply_damage" and item.size)
        code = bytes(binary.get_content_from_virtual_address(symbol.value, symbol.size))
        decoder = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
        instructions = list(decoder.disasm(code, symbol.value))
        if not instructions or sum(item.size for item in instructions) != len(code):
            raise RuntimeError("Fixture function was not fully decoded")

        # Load only the library just compiled from this repository's fixture.
        library = ctypes.CDLL(str(library_path))
        library.apply_damage.argtypes = [ctypes.POINTER(Player), ctypes.c_int32]
        library.apply_damage.restype = None
        library.award_points.argtypes = [ctypes.POINTER(Player), ctypes.c_int32]
        library.award_points.restype = None
        state = Player(100, 0)
        library.apply_damage(ctypes.byref(state), 25)
        if state.health != 75:
            raise RuntimeError("Baseline health mismatch")
        state.health = 150  # Deliberate change to our own test object's memory.
        library.apply_damage(ctypes.byref(state), 25)
        if state.health != 125:
            raise RuntimeError("Controlled state modification mismatch")
        library.apply_damage(ctypes.byref(state), -10)
        if state.health != 125:
            raise RuntimeError("Negative damage was not rejected")
        library.apply_damage(ctypes.byref(state), 1000)
        if state.health != 0:
            raise RuntimeError("Health floor mismatch")
        library.award_points(ctypes.byref(state), 50)
        library.award_points(ctypes.byref(state), -5)
        if state.score != 50:
            raise RuntimeError("Score control mismatch")

        return {
            "checks": {
                "compiled_owned_fixture": "passed",
                "function_bytes_fully_disassembled": "passed",
                "controlled_state_modification": "passed",
                "negative_damage_and_health_floor": "passed",
                "score_input_control": "passed",
            },
            "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "binary_sha256": hashlib.sha256(library_path.read_bytes()).hexdigest(),
            "function": "apply_damage",
            "function_bytes": len(code),
            "instruction_count": len(instructions),
            "player_size": ctypes.sizeof(Player),
            "health_offset": Player.health.offset,
            "score_offset": Player.score.offset,
            "scope": "Own ctypes object and own freshly compiled library; no external process access",
        }


def license_lab():
    private = Ed25519PrivateKey.generate()
    public = private.public_key()
    now = 1000  # Fixed synthetic clock; no dependency on the machine's clock.

    def issue(claims):
        payload = json.dumps(claims, sort_keys=True, separators=(",", ":")).encode()
        return payload, private.sign(payload)

    def accepted(payload, signature, application="owned-lab"):
        try:
            public.verify(signature, payload)
        except InvalidSignature:
            return False
        claims = json.loads(payload)
        return (
            claims["application"] == application
            and claims["expires_at"] > now
            and "practice" in claims["features"]
        )

    claims = {"application": "owned-lab", "expires_at": 2000, "features": ["practice"]}
    payload, signature = issue(claims)
    if not accepted(payload, signature):
        raise RuntimeError("Synthetic valid license rejected")
    altered = payload.replace(b"2000", b"9000")
    if accepted(altered, signature):
        raise RuntimeError("Altered synthetic license accepted")
    expired_payload, expired_signature = issue({**claims, "expires_at": 999})
    if accepted(expired_payload, expired_signature):
        raise RuntimeError("Expired synthetic license accepted")
    if accepted(payload, signature, application="other-lab"):
        raise RuntimeError("Wrong application accepted")
    missing_payload, missing_signature = issue({**claims, "features": []})
    if accepted(missing_payload, missing_signature):
        raise RuntimeError("Missing feature accepted")
    return {
        "checks": {
            "valid_synthetic_license": "passed",
            "tampered_claim_rejected": "passed",
            "expired_license_rejected": "passed",
            "wrong_application_rejected": "passed",
            "missing_feature_rejected": "passed",
        },
        "scope": "Own signed fixtures; keys remain ephemeral; no commercial licensing tested",
    }


if __name__ == "__main__":
    if platform.system() != "Linux" or platform.machine() != "x86_64":
        raise RuntimeError("This exercise currently targets Linux x86-64")
    root = Path(__file__).resolve().parent.parent
    report = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "platform": platform.system(),
        "architecture": platform.machine(),
        "game_state_lab": game_lab(root),
        "license_lab": license_lab(),
        "limitations": "Educational fixtures only; no external memory scanning, injection, anti-cheat evasion or commercial crack tested",
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))

