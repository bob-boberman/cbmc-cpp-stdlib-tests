#include <clocale>

int main() {
    return (std::setlocale(LC_ALL, "C") != nullptr) ? 0 : 1;
}
