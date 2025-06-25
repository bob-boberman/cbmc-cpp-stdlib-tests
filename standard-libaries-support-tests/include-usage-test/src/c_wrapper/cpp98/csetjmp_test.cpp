#include <csetjmp>

jmp_buf buf;

int main() {
    if (setjmp(buf) == 0) {
        longjmp(buf, 1);
    } else {
        return 0;  // Success: longjmp brought us here
    }
    return 1;  // Shouldn't reach here
}
