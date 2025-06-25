#include <concepts>
template <std::integral T> void f(T) {}
int main() { f(1); return 0; }
