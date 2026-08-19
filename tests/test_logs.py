from linux.logs import (
    get_recent_logs,
    get_error_logs,
    get_kernel_logs,
    get_log_status
)


print("Recent Logs:")
recent = get_recent_logs(10)

print("Success:", recent["success"])
print("Error:", recent["error"])

for log in recent["logs"]:
    print(log)


print("\nRecent Error Logs:")
errors = get_error_logs(10)

print("Success:", errors["success"])
print("Error:", errors["error"])

for log in errors["logs"]:
    print(log)


print("\nKernel Logs:")
kernel = get_kernel_logs(10)

print("Success:", kernel["success"])
print("Error:", kernel["error"])

for log in kernel["logs"]:
    print(log)


print("\nComplete Log Status:")
print(get_log_status())
