#include <charconv>
char buf[10];
int main() { int v; std::from_chars(buf, buf+10, v); return 0; }
