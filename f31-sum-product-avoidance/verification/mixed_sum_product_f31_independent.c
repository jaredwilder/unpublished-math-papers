/* Independent exhaustive verifier for simultaneous sum/product-free subsets
   of F_31^*. This implementation tests x+y=z and xy=z directly. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define P 31
#define N 30
#define MAX_EXT 32

static uint64_t count_by_size[N + 1];
static uint32_t extremizers[MAX_EXT];
static size_t extremizer_count = 0;
static int maximum = 0;
static uint64_t search_nodes = 0;

static int contains(uint32_t mask, int value) {
    return value > 0 && value < P && ((mask >> (value - 1)) & 1U) != 0U;
}

static int can_add(uint32_t mask, int v) {
    uint32_t candidate = mask | (1U << (v - 1));
    for (int x = 1; x < P; ++x) {
        if (!contains(candidate, x)) continue;
        for (int y = 1; y < P; ++y) {
            if (!contains(candidate, y)) continue;
            int sum = (x + y) % P;
            int product = (x * y) % P;
            if (contains(candidate, sum) || contains(candidate, product)) return 0;
        }
    }
    return 1;
}

static void visit(uint32_t mask, int next, int size) {
    ++search_nodes;
    ++count_by_size[size];
    if (size > maximum) {
        maximum = size;
        extremizer_count = 0;
    }
    if (size == maximum && extremizer_count < MAX_EXT) {
        extremizers[extremizer_count++] = mask;
    }
    for (int v = next; v < P; ++v) {
        if (can_add(mask, v)) visit(mask | (1U << (v - 1)), v + 1, size + 1);
    }
}

static int compare_u32(const void *a, const void *b) {
    uint32_t x = *(const uint32_t *)a, y = *(const uint32_t *)b;
    return (x > y) - (x < y);
}

static void print_set(uint32_t mask) {
    int first = 1;
    putchar('[');
    for (int v = 1; v < P; ++v) {
        if (contains(mask, v)) {
            if (!first) putchar(',');
            printf("%d", v);
            first = 0;
        }
    }
    putchar(']');
}

int main(void) {
    memset(count_by_size, 0, sizeof(count_by_size));
    visit(0U, 1, 0);
    qsort(extremizers, extremizer_count, sizeof(uint32_t), compare_u32);
    if (maximum != 8 || count_by_size[8] != 9 || count_by_size[9] != 0 || extremizer_count != 9) {
        fprintf(stderr, "unexpected classification\n");
        return 2;
    }
    printf("prime=31\n");
    printf("maximum=8\n");
    printf("extremal_count=9\n");
    printf("next_layer_count=0\n");
    printf("search_nodes=%llu\n", (unsigned long long)search_nodes);
    for (int k = 0; k <= maximum + 1; ++k) {
        printf("valid_size_%d_count=%llu\n", k, (unsigned long long)count_by_size[k]);
    }
    for (size_t i = 0; i < extremizer_count; ++i) {
        printf("extremizer_%zu=", i + 1U);
        print_set(extremizers[i]);
        putchar('\n');
    }
    printf("status=PASS\n");
    return 0;
}
