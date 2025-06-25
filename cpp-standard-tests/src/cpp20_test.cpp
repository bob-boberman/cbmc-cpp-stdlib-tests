// C++20: concepts, consteval, constinit, designated initializers, ranges-based for with initializer

template <typename T>
concept Addable = requires(T a, T b) {
    a + b;
};

consteval int always_five() {
    return 5;
}

struct Point {
    int x;
    int y;
};

constinit int global_value = 20;

int main() {
    static_assert(Addable<int>);
    int arr[3] = {1, 2, 3};
    int sum = 0;
    for (int v : arr)
        sum += v;

    Point p = {.x = 1, .y = 2};

    int val = always_five();

    return (sum == 6 && p.x == 1 && p.y == 2 && val == 5 && global_value == 20) ? 0 : 1;
}
