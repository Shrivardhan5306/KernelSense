import subprocess


def execute_command(command):
    """
    Execute a Linux command without using a shell.
    """

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
            check=False
        )

        return {
            "success": result.returncode == 0,
            "return_code": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "return_code": None,
            "stdout": "",
            "stderr": "Command timed out"
        }

    except FileNotFoundError:
        return {
            "success": False,
            "return_code": None,
            "stdout": "",
            "stderr": "Command not found"
        }

    except OSError as error:
        return {
            "success": False,
            "return_code": None,
            "stdout": "",
            "stderr": str(error)
        }
