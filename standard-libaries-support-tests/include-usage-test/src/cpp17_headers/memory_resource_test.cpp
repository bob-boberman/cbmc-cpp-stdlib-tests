#include <memory_resource>

int main() {
    char buffer[1024];
    std::pmr::monotonic_buffer_resource resource(buffer, sizeof(buffer));
    std::pmr::polymorphic_allocator<int> alloc(&resource);
    int* p = alloc.allocate(1);
    alloc.deallocate(p, 1);
    return 0;
}
