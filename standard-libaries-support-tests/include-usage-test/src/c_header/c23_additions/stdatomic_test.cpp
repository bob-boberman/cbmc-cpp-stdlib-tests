#include <stdatomic.h>

int main() {
    atomic_int x;
    atomic_init(&x, 0);
    atomic_fetch_add(&x, 1);
    return (atomic_load(&x) == 1) ? 0 : 1;
}
