#include <complex.h>

int main() {
    double _Complex z = 1.0 + 1.0 * I;
    return (creal(z) == 1.0) ? 0 : 1;
}
