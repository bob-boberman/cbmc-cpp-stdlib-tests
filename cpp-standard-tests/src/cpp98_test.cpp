// C++98: namespaces, templates, bool, inline, operator overloading, member initializer list

namespace myns {
inline int add(int a, int b) {
    return a + b;
}

template <typename T>
T mul(T a, T b) {
    return a * b;
}
}  // namespace myns

class MyClass {
    int value;

   public:
    MyClass(int v) : value(v) {}

    bool operator==(const MyClass& other) const {
        return value == other.value;
    }

    int get() const {
        return value;
    }
};

int main() {
    bool b = true;
    int x = myns::add(2, 3);
    int y = myns::mul<int>(4, 5);

    MyClass a(10), b2(10);
    bool eq = (a == b2);

    return (b && x == 5 && y == 20 && eq && a.get() == 10) ? 0 : 1;
}
