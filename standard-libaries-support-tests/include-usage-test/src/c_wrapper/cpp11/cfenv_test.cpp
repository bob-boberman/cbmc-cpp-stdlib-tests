#include <cfenv>
int main() { std::feclearexcept(FE_ALL_EXCEPT); return 0; }
