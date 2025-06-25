#include <latch>
int main() { std::latch l(1); l.count_down(); return 0; }
