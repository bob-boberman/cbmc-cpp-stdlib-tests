#include <cstdarg>

int sum(int count, ...) {
    va_list args;
    va_start(args, count);
    int total = 0;
    for (int i = 0; i < count; ++i)
        total += va_arg(args, int);
    va_end(args);
    return total;
}

int main() {
    return (sum(2, 1, 2) == 3) ? 0 : 1;
}
