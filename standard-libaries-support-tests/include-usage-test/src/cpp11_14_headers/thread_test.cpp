#include <thread>
void f() {}
int main() { std::thread t(f); t.join(); return 0; }
