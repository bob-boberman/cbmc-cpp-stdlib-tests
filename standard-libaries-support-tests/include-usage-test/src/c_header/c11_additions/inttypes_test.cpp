#include <inttypes.h>
#include <stdio.h>

int main() {
    intmax_t x = 123;
    printf("%" PRIdMAX "\n", x);
    return 0;
}
