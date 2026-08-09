import psutil


def get_root_disk_usage():
    """Return usage information for the root filesystem."""
    disk = psutil.disk_usage("/")

    return {
        "total_bytes": disk.total,
        "used_bytes": disk.used,
        "free_bytes": disk.free,
        "usage_percent": disk.percent
    }


def get_mounted_filesystems():
    """Return information about mounted filesystems."""
    filesystems = []

    for partition in psutil.disk_partitions(all=False):
        try:
            usage = psutil.disk_usage(partition.mountpoint)

            filesystems.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "filesystem": partition.fstype,
                "total_bytes": usage.total,
                "used_bytes": usage.used,
                "free_bytes": usage.free,
                "usage_percent": usage.percent
            })

        except (PermissionError, OSError):
            continue

    return filesystems


def get_storage_status():
    """Return complete storage information."""
    return {
        "root": get_root_disk_usage(),
        "filesystems": get_mounted_filesystems()
    }
