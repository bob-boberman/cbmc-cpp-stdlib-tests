#include <fenv.h>

int main() {
    return (feclearexcept(FE_ALL_EXCEPT) == 0) ? 0 : 1;
}
