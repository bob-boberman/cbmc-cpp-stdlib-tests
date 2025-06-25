#include <stdalign.h>

int main() {
    alignas(16) int x;
    return ((alignof(x) >= 4) ? 0 : 1);
}
