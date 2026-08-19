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
    Validate command name and arguments.
    """

    if not command:
        return {
            "allowed": False,
            "requires_approval": False,
            "risk": "critical",
            "reason": "Empty command"
        }

    executable = command[0]

    # Always block explicitly dangerous commands.
    if executable in CRITICAL_COMMANDS:
        return {
            "allowed": False,
            "requires_approval": False,
            "risk": "critical",
            "reason": "Critical command is blocked"
        }

    # Medium-risk commands require user approval.
    if executable in MEDIUM_COMMANDS:
        return {
            "allowed": False,
            "requires_approval": True,
            "risk": "medium",
            "reason": "User approval is required"
        }

    # Unknown commands are denied by default.
    if executable not in SAFE_COMMANDS:
        return {
            "allowed": False,
            "requires_approval": False,
            "risk": "unknown",
            "reason": "Command is not in the allowlist"
        }

    # Basic argument validation.
    dangerous_arguments = {
        "|",
        "||",
        "&&",
        ";",
        ">",
        ">>",
        "<",
        "$(",
        "`",
    }

    for argument in command[1:]:
        if argument in dangerous_arguments:
            return {
                "allowed": False,
                "requires_approval": False,
                "risk": "critical",
                "reason": "Shell control argument is blocked"
            }

    return {
        "allowed": True,
        "requires_approval": False,
        "risk": "safe",
        "reason": "Command and arguments passed validation"
    }
