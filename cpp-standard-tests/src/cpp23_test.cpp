// C++23: deducing this, static operator(), explicit object parameter, if consteval

struct Counter {
    int value = 0;

    void inc(this Counter& self) {
        self.value++;
    }  // deducing this

    static int call() {
        return 23;
    }

    static int call_static() requires true {
        return 42;
    }
};

int main() {
    Counter c;
    c.inc();
    int v = 0;
    if consteval {
        v = 1;
    } else {
        v = 2;
    }
    int s = Counter::call();
    int t = Counter::call_static();

    return (c.value == 1 && (v == 1 || v == 2) && s == 23 && t == 42) ? 0 : 1;
}
