from linux.network import (
    get_network_interfaces,
    get_network_statistics,
    check_internet_connection,
    get_network_status
)


print("Network Interfaces:")
for interface in get_network_interfaces():
    print(interface)


print("\nNetwork Statistics:")
print(get_network_statistics())


print("\nInternet Connection:")
print(check_internet_connection())


print("\nComplete Network Status:")
print(get_network_status())
