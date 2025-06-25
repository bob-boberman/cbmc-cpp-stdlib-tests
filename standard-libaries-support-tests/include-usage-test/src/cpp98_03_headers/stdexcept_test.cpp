#include <stdexcept>
int main() { try { throw std::runtime_error("err"); } catch(...) {} return 0; }
