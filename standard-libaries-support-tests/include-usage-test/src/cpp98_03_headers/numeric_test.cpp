#include <numeric>
int main() { int a[2] = {1,2}; return std::accumulate(a,a+2,0); }
