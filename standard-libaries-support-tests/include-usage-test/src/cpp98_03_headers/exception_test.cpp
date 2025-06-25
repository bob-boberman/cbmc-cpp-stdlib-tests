#include <exception>
int main() { try { throw std::exception(); } catch(...) {} return 0; }
