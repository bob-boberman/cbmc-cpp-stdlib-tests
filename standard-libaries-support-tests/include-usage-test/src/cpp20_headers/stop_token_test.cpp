#include <stop_token>
int main() { std::stop_source src; auto tok = src.get_token(); return 0; }
