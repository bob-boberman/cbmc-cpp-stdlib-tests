#include <time.h>

int main() {
    return (time(NULL) != (time_t)(-1)) ? 0 : 1;
}
