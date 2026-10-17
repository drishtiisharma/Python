
#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#include <time.h>

void copy_key(uint64_t key) {
    printf("Copy Value: %" PRIu64 "\n", key);
}

void check_key(const uint64_t *ptr) {
    printf("Pointer Value: %" PRIu64 "\n", *ptr);
}

int main() {
    uint64_t key = 987254810ULL;
    clock_t start, end;

    start = clock();
    copy_key(key);
    end = clock();
    printf("Copy Time: %f sec\n", (double)(end - start) / CLOCKS_PER_SEC);

    start = clock();
    check_key(&key);
    end = clock();
    printf("Pointer Time: %f sec\n", (double)(end - start) / CLOCKS_PER_SEC);

    return 0;
}





