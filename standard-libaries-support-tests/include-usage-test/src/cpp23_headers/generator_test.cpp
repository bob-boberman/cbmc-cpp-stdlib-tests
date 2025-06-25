#include <generator>

std::generator<int> simple_gen() {
    co_yield 1;
    co_yield 2;
}

int main() {
    for (int x : simple_gen()) {
        (void)x;
    }

    return 0;
}
