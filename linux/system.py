import getpass
import platform
import socket
import time

import psutil


def get_os_info():
    """Return operating system information."""
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "distribution": platform.platform(),
        "architecture": platform.machine(),
    }


def get_hostname():
    """Return the system hostname."""
    return socket.gethostname()


def get_current_user():
    """Return the current Linux user."""
    return getpass.getuser()


def get_uptime():
    """Return system uptime information."""
    boot_time = psutil.boot_time()
    current_time = time.time()

    uptime_seconds = current_time - boot_time

    return {
        "boot_time": boot_time,
        "uptime_seconds": uptime_seconds,
    }


def get_system_status():
    """Return complete system information."""
    return {
        "os": get_os_info(),
        "hostname": get_hostname(),
        "user": get_current_user(),
        "uptime": get_uptime(),
    }
