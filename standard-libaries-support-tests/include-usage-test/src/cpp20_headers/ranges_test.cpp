#include <ranges>
int main() { int a[2] = {1,2}; auto v = a | std::views::all; return 0; }
