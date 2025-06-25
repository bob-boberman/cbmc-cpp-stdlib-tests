#include <cstdalign>

int main() {
    alignas(16) char buffer[16];
    (void)buffer;  // suppress unused warning
    return 0;
}
