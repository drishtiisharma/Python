#include <stdio.h>
#include <stdint.h>

int main() {
    int a = -1;
    uint32_t b = -1;

    printf("int: %d\n", a);
    printf("uint32_t: %u\n", b);

    printf("int size: %zu bytes\n", sizeof(a));
    printf("uint32_t size: %zu bytes\n", sizeof(b));

    return 0;
}
