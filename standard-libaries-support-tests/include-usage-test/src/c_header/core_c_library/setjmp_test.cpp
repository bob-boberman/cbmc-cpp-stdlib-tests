#include <setjmp.h>

int main() {
    jmp_buf buf;
    if (setjmp(buf) == 0) {
        longjmp(buf, 1);
    }
    return 0;
}
