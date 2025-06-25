#include <wchar.h>

int main() {
    wchar_t wstr[] = L"test";
    return (wcslen(wstr) == 4) ? 0 : 1;
}
