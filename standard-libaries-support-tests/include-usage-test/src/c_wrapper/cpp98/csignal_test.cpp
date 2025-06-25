#include <csignal>

int main() {
    std::signal(SIGINT, SIG_DFL);
    return 0;
}
