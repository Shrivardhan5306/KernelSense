from linux.storage import (
    get_root_disk_usage,
    get_mounted_filesystems,
    get_storage_status
)


print("Root Disk Usage:")
print(get_root_disk_usage())

print("\nMounted Filesystems:")
for filesystem in get_mounted_filesystems():
    print(filesystem)

print("\nComplete Storage Status:")
print(get_storage_status())
