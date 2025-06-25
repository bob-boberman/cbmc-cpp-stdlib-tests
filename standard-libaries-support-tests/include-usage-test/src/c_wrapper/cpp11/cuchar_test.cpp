#include <cuchar>

int main() {
    char16_t src[] = u"hi";
    char mb[10]{};
    mbstate_t state{};
    std::c16rtomb(mb, src[0], &state);
    return 0;
}
