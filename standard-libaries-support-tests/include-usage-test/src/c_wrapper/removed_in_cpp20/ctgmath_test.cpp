#include <ctgmath>

int main() {
    double x = 0.5;
    double y = sin(x);  // type-generic sin
    (void)y;            // suppress unused warning
    return 0;
}
