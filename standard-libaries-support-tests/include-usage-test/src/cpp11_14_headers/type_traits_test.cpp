#include <type_traits>
int main() { bool b = std::is_integral<int>::value; return b ? 0 : 1; }
