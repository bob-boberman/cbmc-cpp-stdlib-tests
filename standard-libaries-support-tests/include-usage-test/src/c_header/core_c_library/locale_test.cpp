#include <locale.h>

int main() {
    return setlocale(LC_ALL, "") ? 0 : 1;
}
