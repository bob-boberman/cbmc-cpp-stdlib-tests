#include <functional>

int add(int a, int b) {
    return a + b;
}

int main() {
    std::plus<int> plus_op;
    std::minus<int> minus_op;
    std::multiplies<int> multiplies_op;
    std::negate<int> negate_op;

    int a = 5, b = 3;

    // Use function objects
    int sum = plus_op(a, b);
    int diff = minus_op(a, b);
    int prod = multiplies_op(a, b);
    int neg = negate_op(a);

    // Use std::function with a function pointer
    std::function<int(int, int)> func_ptr = add;
    int sum2 = func_ptr(2, 4);

    // Use std::function with a lambda
    std::function<int(int, int)> lambda = [](int x, int y) {
        return x * y;
    };
    int prod2 = lambda(3, 7);

    // Return 0 if all results are as expected
    return (sum == 8 && diff == 2 && prod == 15 && neg == -5 && sum2 == 6 && prod2 == 21) ? 0 : 1;
}
