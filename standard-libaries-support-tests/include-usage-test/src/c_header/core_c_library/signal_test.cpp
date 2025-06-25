#include <signal.h>

void handler(int) {}

int main() {
    return (signal(SIGINT, handler) != SIG_ERR) ? 0 : 1;
}
