#include <spanstream>

int main() {
    char buffer[16]{};
    std::spanstream ss(buffer, std::size(buffer));

    ss << 42;
    int x = 0;
    ss >> x;

    (void)x;
    return 0;
}