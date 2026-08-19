import subprocess
import time


def execute_command(command):
    """
    Execute a Linux command without using a shell.
    """

    start_time = time.perf_counter()

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
            check=False
        )

        execution_time_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        return {
            "command": command,
            "success": result.returncode == 0,
            "return_code": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "execution_time_ms": execution_time_ms
        }

    except subprocess.TimeoutExpired:

        execution_time_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        return {
            "command": command,
            "success": False,
            "return_code": None,
            "stdout": "",
            "stderr": "Command timed out",
            "execution_time_ms": execution_time_ms
        }

    except FileNotFoundError:

        execution_time_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        return {
            "command": command,
            "success": False,
            "return_code": None,
            "stdout": "",
            "stderr": "Command not found",
            "execution_time_ms": execution_time_ms
        }

    except OSError as error:

        execution_time_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        return {
            "command": command,
            "success": False,
            "return_code": None,
            "stdout": "",
            "stderr": str(error),
            "execution_time_ms": execution_time_ms
        }
