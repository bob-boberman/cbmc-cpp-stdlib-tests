#include <stacktrace>

int main() {
    auto st = std::stacktrace::current();
    (void)st;
    return 0;
}