// C++11: auto, nullptr, lambda, range-based for, static_assert, enum class, move semantics

class MoveOnly {
    int value;

   public:
    MoveOnly(int v) : value(v) {}

    MoveOnly(MoveOnly&& other) : value(other.value) {
        other.value = 0;
    }

    MoveOnly& operator=(MoveOnly&& other) {
        value = other.value;
        other.value = 0;
        return *this;
    }

    int get() const {
        return value;
    }
};

enum class Color {
    Red,
    Green,
    Blue
};

int main() {
    auto x = 42;
    int arr[3] = {1, 2, 3};
    int sum = 0;
    for (auto v : arr)
        sum += v;

    auto lam = [](int a, int b) {
        return a + b;
    };
    int y = lam(2, 3);

    static_assert(sizeof(int) == 4 || sizeof(int) == 8, "int size");

    Color c = Color::Red;

    MoveOnly m1(5);
    MoveOnly m2 = static_cast<MoveOnly&&>(m1);

    return (x == 42 && sum == 6 && y == 5 && m2.get() == 5 && c == Color::Red) ? 0 : 1;
}
