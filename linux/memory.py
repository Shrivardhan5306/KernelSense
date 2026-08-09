import psutil


def get_memory_info():
    """Return RAM usage information."""
    memory = psutil.virtual_memory()

    return {
        "total_bytes": memory.total,
        "available_bytes": memory.available,
        "used_bytes": memory.used,
        "free_bytes": memory.free,
        "usage_percent": memory.percent
    }


def get_swap_info():
    """Return swap memory information."""
    swap = psutil.swap_memory()

    return {
        "total_bytes": swap.total,
        "used_bytes": swap.used,
        "free_bytes": swap.free,
        "usage_percent": swap.percent
    }


def get_memory_status():
    """Return complete RAM and swap information."""
    return {
        "memory": get_memory_info(),
        "swap": get_swap_info()
    }
