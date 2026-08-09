from linux.system import (
    get_os_info,
    get_hostname,
    get_current_user,
    get_uptime,
    get_system_status
)


print("OS Information:")
print(get_os_info())

print("\nHostname:")
print(get_hostname())

print("\nCurrent User:")
print(get_current_user())

print("\nUptime:")
print(get_uptime())

print("\nComplete System Status:")
print(get_system_status())
