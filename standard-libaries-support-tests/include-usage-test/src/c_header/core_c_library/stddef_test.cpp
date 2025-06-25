#include <stddef.h>

struct S {
    char c;
    int i;
};

int main() {
    size_t size = sizeof(int);
    ptrdiff_t diff = (char*)&((S*)0)->i - (char*)&((S*)0)->c;
    size_t offset = offsetof(S, i);

    return (offset == diff && size > 0) ? 0 : 1;
}
