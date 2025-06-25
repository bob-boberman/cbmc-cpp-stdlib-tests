#include <ciso646>

int main() {
    bool a = true;
    bool b = false;
    if (a and not b) {
        return 0;
    }
    return 1;
}
