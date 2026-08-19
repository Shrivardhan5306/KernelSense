import subprocess


def run_journalctl(args):
    """Run journalctl safely and return its output."""
    command = ["journalctl", "--no-pager"] + args

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
            check=False
        )

        if result.returncode != 0:
            return {
                "success": False,
                "error": result.stderr.strip(),
                "logs": []
            }

        return {
            "success": True,
            "error": None,
            "logs": result.stdout.splitlines()
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "journalctl command timed out",
            "logs": []
        }

    except FileNotFoundError:
        return {
            "success": False,
            "error": "journalctl is not available",
            "logs": []
        }

    except OSError as error:
        return {
            "success": False,
            "error": str(error),
            "logs": []
        }


def get_recent_logs(limit=50):
    """Return the most recent system logs."""
    return run_journalctl(["-n", str(limit)])


def get_error_logs(limit=50):
    """Return recent error-level logs."""
    return run_journalctl([
        "-p",
        "err",
        "-n",
        str(limit)
    ])


def get_kernel_logs(limit=50):
    """Return recent kernel logs."""
    return run_journalctl([
        "-k",
        "-n",
        str(limit)
    ])


def get_service_logs(service, limit=50):
    """Return logs for a specific systemd service."""
    return run_journalctl([
        "-u",
        service,
        "-n",
        str(limit)
    ])


def get_log_status():
    """Return a summary of available log information."""
    recent = get_recent_logs(20)
    errors = get_error_logs(20)

    return {
        "journal_available": recent["success"],
        "recent_logs": recent["logs"],
        "recent_errors": errors["logs"],
        "error_query_success": errors["success"]
    }
