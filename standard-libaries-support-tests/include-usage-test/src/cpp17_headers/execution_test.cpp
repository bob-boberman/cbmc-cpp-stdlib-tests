#include <execution>

int main() {
    // The <execution> header itself does not provide any functionality without an algorithm.
    // So, just a minimal usage:
    auto policy = std::execution::seq;
    (void)policy;  // Suppress unused variable warning
    return 0;
}
