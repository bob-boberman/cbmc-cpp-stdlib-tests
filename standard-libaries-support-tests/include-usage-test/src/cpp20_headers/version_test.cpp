#include <version>

int main() {
#ifdef __cpp_lib_format
    return __cpp_lib_format;
#elif defined(__cpp_lib_ranges)
    return __cpp_lib_ranges;
#elif defined(__cpp_lib_concepts)
    return __cpp_lib_concepts;
#else
    return 0;
#endif
}
