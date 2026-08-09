import platform
import psutil


def get_cpu_usage():
    """Return current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)


def get_cpu_count():
    """Return physical and logical CPU core counts."""
    return {
        "physical": psutil.cpu_count(logical=False),
        "logical": psutil.cpu_count(logical=True)
    }


def get_cpu_frequency():
    """Return current CPU frequency in MHz."""
    frequency = psutil.cpu_freq()

    if frequency is None:
        return None

    return {
        "current_mhz": frequency.current,
        "min_mhz": frequency.min,
        "max_mhz": frequency.max
    }


def get_cpu_info():
    """Return basic CPU information."""
    return {
        "processor": platform.processor(),
        "architecture": platform.machine()
    }


def get_cpu_temperature():
    """Return CPU temperature when supported."""
    try:
        temperatures = psutil.sensors_temperatures()

        if not temperatures:
            return None

        result = {}

        for sensor_name, entries in temperatures.items():
            result[sensor_name] = [
                {
                    "label": entry.label,
                    "current": entry.current,
                    "high": entry.high,
                    "critical": entry.critical
                }
                for entry in entries
            ]

        return result

    except (AttributeError, NotImplementedError):
        return None


def get_cpu_status():
    """Return complete CPU information."""
    return {
        "usage_percent": get_cpu_usage(),
        "cores": get_cpu_count(),
        "frequency": get_cpu_frequency(),
        "info": get_cpu_info(),
        "temperature": get_cpu_temperature()
    }
