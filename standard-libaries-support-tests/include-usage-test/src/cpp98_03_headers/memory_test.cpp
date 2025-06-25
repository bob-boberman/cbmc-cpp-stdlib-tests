#include <memory>
int main() { std::unique_ptr<int> p(new int(1)); return 0; }
