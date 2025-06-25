#include <cerrno>

int main() {
    errno = 0;       // Set errno to 0
    int e1 = errno;  // Read errno (should be 0)
    errno = 5;       // Set errno to a specific error code
    int e2 = errno;  // Read errno (should be 5)
    return e1 + e2;  // Use the values to avoid unused variable warnings
}
