#include <flat_set>

int main() {
    std::flat_set<int> fs;
    fs.insert(1);
    fs.insert(2);

    for (int x : fs) {
        (void)x;
    }

    return 0;
}
