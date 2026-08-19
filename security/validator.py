SAFE_COMMANDS = {
    "pwd",
    "ls",
    "df",
    "du",
    "ps",
    "free",
    "uptime",
    "whoami",
    "hostname",
    "uname",
    "ip",
}

MEDIUM_COMMANDS = {
    "systemctl",
    "journalctl",
    "apt",
    "apt-get",
}

CRITICAL_COMMANDS = {
    "rm",
    "rmdir",
    "mkfs",
    "mkfs.ext4",
    "dd",
    "shutdown",
    "reboot",
    "poweroff",
    "halt",
    "kill",
    "pkill",
}


def validate_command(command):
    """
    Classify a Linux command according to the KernelSense
    security policy.
    """

    if not command:
        return {
            "allowed": False,
            "requires_approval": False,
            "risk": "critical",
            "reason": "Empty command"
        }

    executable = command[0]

    if executable in CRITICAL_COMMANDS:
        return {
            "allowed": False,
            "requires_approval": False,
            "risk": "critical",
            "reason": "Critical command is blocked"
        }

    if executable in MEDIUM_COMMANDS:
        return {
            "allowed": False,
            "requires_approval": True,
            "risk": "medium",
            "reason": "User approval is required"
        }

    if executable in SAFE_COMMANDS:
        return {
            "allowed": True,
            "requires_approval": False,
            "risk": "safe",
            "reason": "Command is in the safe allowlist"
        }

    return {
        "allowed": False,
        "requires_approval": False,
        "risk": "unknown",
        "reason": "Command is not in the allowlist"
    }
