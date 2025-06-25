#include <new>

int main() {
    alignas(int) char buffer[sizeof(int)];
    int* p = new (static_cast<void*>(buffer)) int(42);
    return 0;
}
