import psutil


def get_running_processes():
    """Return information about currently running processes."""
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "username", "status", "cpu_percent", "memory_percent"]
    ):
        try:
            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"],
                "username": info["username"],
                "status": info["status"],
                "cpu_percent": info["cpu_percent"],
                "memory_percent": info["memory_percent"]
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return processes


def get_top_cpu_processes(limit=10):
    """Return processes using the most CPU."""
    processes = get_running_processes()

    processes.sort(
        key=lambda process: process["cpu_percent"] or 0,
        reverse=True
    )

    return processes[:limit]


def get_top_memory_processes(limit=10):
    """Return processes using the most memory."""
    processes = get_running_processes()

    processes.sort(
        key=lambda process: process["memory_percent"] or 0,
        reverse=True
    )

    return processes[:limit]


def get_process_status():
    """Return a summary of running processes."""
    processes = get_running_processes()

    return {
        "total_processes": len(processes),
        "top_cpu": get_top_cpu_processes(),
        "top_memory": get_top_memory_processes()
    }
