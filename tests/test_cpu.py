from linux.cpu import (
    get_cpu_usage,
    get_cpu_count,
    get_cpu_frequency,
    get_cpu_info,
    get_cpu_temperature,
    get_cpu_status
)


print("CPU Usage:")
print(get_cpu_usage())

print("\nCPU Count:")
print(get_cpu_count())

print("\nCPU Frequency:")
print(get_cpu_frequency())

print("\nCPU Info:")
print(get_cpu_info())

print("\nCPU Temperature:")
print(get_cpu_temperature())

print("\nComplete CPU Status:")
print(get_cpu_status())
