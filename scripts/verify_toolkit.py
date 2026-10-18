"""Verify the local toolkit with synthetic data; optionally query public PyPI metadata."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from datetime import datetime, timezone
from urllib.request import urlopen

import capstone
import lief
from cryptography.exceptions import InvalidSignature, InvalidTag
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from elftools.elf.elffile import ELFFile


def verify(check_updates=False):
    projects = ("capstone", "lief", "pyelftools", "cryptography")
    installed = {name: importlib.metadata.version(name) for name in projects}
    checks = {}

    # Synthetic x86-64 bytes, not code extracted from any third-party target.
    decoder = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
    instructions = list(decoder.disasm(bytes.fromhex("b801000000c3"), 0x1000))
    if [item.mnemonic for item in instructions] != ["mov", "ret"]:
        raise RuntimeError("Synthetic disassembly mismatch")
    checks["synthetic_x86_64_disassembly"] = "passed"

    # Read the running interpreter as an ELF fixture; never execute an unknown target.
    binary = lief.parse(sys.executable)
    if not isinstance(binary, lief.ELF.Binary):
        raise RuntimeError("This verification requires a Linux ELF interpreter")
    with open(sys.executable, "rb") as stream:
        header = ELFFile(stream)
        if header.elfclass != 64 or not binary.sections:
            raise RuntimeError("Unexpected ELF fixture layout")
    with open(sys.executable, "rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    checks["elf_read_lief_and_pyelftools"] = "passed"

    # Ephemeral keys stay in memory and are never printed or saved.
    from os import urandom

    cipher = AESGCM(AESGCM.generate_key(bit_length=256))
    nonce = urandom(12)
    plaintext = b"Synthetic reverse engineering laboratory fixture"
    associated = b"lab-v1"
    ciphertext = cipher.encrypt(nonce, plaintext, associated)
    if cipher.decrypt(nonce, ciphertext, associated) != plaintext:
        raise RuntimeError("AEAD roundtrip mismatch")
    changed = ciphertext[:-1] + bytes([ciphertext[-1] ^ 1])
    try:
        cipher.decrypt(nonce, changed, associated)
    except InvalidTag:
        checks["aes_gcm_roundtrip_and_tamper_rejection"] = "passed"
    else:
        raise RuntimeError("AEAD failed to reject altered data")

    private = Ed25519PrivateKey.generate()
    signature = private.sign(plaintext)
    public = private.public_key()
    public.verify(signature, plaintext)
    try:
        public.verify(signature, plaintext + b"changed")
    except InvalidSignature:
        checks["ed25519_signature_and_tamper_rejection"] = "passed"
    else:
        raise RuntimeError("Signature accepted altered message")

    updates = {}
    if check_updates:
        for name in projects:
            # Fixed public metadata endpoints only; no credentials or custom URLs.
            try:
                with urlopen(f"https://pypi.org/pypi/{name}/json", timeout=20) as response:
                    latest = json.load(response)["info"]["version"]
                updates[name] = {
                    "pypi_reported_version": latest,
                    "matches_installed": latest == installed[name],
                    "note": "Latest project version may have different platform requirements",
                }
            except Exception as error:
                updates[name] = {"status": "unknown", "error_type": type(error).__name__}

    return {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "platform": platform.system(),
        "architecture": platform.machine(),
        "python": platform.python_version(),
        "installed": installed,
        "checks": checks,
        "elf_fixture": {"identity": "current_python_interpreter", "sha256": digest},
        "pypi_metadata": updates,
        "scope": "Synthetic smoke checks and one local ELF read; no anti-cheat or commercial protection tested",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-updates", action="store_true")
    args = parser.parse_args()
    print(json.dumps(verify(args.check_updates), indent=2, ensure_ascii=False))

