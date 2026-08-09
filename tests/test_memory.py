from linux.memory import (
    get_memory_info,
    get_swap_info,
    get_memory_status
)


print("Memory Information:")
print(get_memory_info())

print("\nSwap Information:")
print(get_swap_info())

print("\nComplete Memory Status:")
print(get_memory_status())
