#include <barrier>
#include <thread>
void f(std::barrier<> &b) { b.arrive_and_wait(); }
int main() { std::barrier<> b(2); std::thread t(f, std::ref(b)); f(b); t.join(); return 0; }
