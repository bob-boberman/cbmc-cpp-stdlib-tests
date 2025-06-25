#include <syncstream>
int main() { std::osyncstream os(std::cout); os << "hi"; return 0; }
