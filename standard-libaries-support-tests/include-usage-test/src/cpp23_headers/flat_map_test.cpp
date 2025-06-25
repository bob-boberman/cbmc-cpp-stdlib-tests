#include <flat_map>

int main() {
    std::flat_map<int, const char*> fm;
    fm[1] = "one";
    fm[2] = "two";

    for (const auto& [key, value] : fm) {
        (void)key;
        (void)value;
    }

    return 0;
}