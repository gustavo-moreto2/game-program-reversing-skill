/* Original synthetic fixture; no third-party game or process is targeted. */
#include <stdint.h>

struct player {
    int32_t health;
    int32_t score;
};

void apply_damage(struct player *state, int32_t damage) {
    if (damage < 0) return;
    if (damage >= state->health) state->health = 0;
    else state->health -= damage;
}

void award_points(struct player *state, int32_t points) {
    if (points >= 0 && points <= 1000) state->score += points;
}

