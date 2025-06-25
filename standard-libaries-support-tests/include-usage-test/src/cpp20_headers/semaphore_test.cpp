#include <semaphore>
int main() { std::counting_semaphore<1> s(1); s.acquire(); s.release(); return 0; }
