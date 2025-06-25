#include <stdlib.h>

int main() {
    int* p = (int*)malloc(sizeof(int));
    if (!p)
        return 1;
    free(p);
    return 0;
}
