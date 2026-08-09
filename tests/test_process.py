from linux.process import (
    get_running_processes,
    get_top_cpu_processes,
    get_top_memory_processes,
    get_process_status
)


print("Number of Running Processes:")
processes = get_running_processes()
print(len(processes))


print("\nTop CPU Processes:")
for process in get_top_cpu_processes():
    print(process)


print("\nTop Memory Processes:")
for process in get_top_memory_processes():
    print(process)


print("\nComplete Process Status:")
print(get_process_status())
