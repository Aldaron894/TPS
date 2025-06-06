#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#define IV  0x80400c0600000000
typedef struct {
    uint64_t *blocks;
    int nb_blocks;
} msg_t;

typedef struct {
    msg_t C;
    uint64_t T[2];
} ciphertext_t;

typedef uint64_t* state_t;
state_t set_initial_state (const uint64_t key[2], const uint64_t nonce[2], uint64_t iv);
void processing_associate_data(state_t S, msg_t A);
