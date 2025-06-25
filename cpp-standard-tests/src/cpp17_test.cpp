// C++17: if constexpr, structured bindings, inline variables, fold expressions

struct S {
    int a;
    double b;
};

template <typename... Args>
int sum(Args... args) {
    return (args + ...);
}

inline int global_var = 17;

int main() {
    S s{1, 2.0};
    auto [x, y] = s;

    int result = 0;
    if constexpr (sizeof(int) == 4 || sizeof(int) == 8) {
        result = 1;
    }

    int folded = sum(1, 2, 3, 4);

    return (x == 1 && y == 2.0 && result == 1 && folded == 10 && global_var == 17) ? 0 : 1;
}
