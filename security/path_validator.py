from pathlib import Path


# Directories that KernelSense should never access.
BLOCKED_PATHS = {
    "/bin",
    "/boot",
    "/dev",
    "/etc",
    "/proc",
    "/sys",
    "/usr",
    "/var",
}


def normalize_path(path):
    """
    Convert a path into an absolute normalized path.
    """
    return Path(path).expanduser().resolve()


def is_blocked_path(path):
    """
    Check whether a path is inside a protected system directory.
    """
    normalized = normalize_path(path)

    for blocked in BLOCKED_PATHS:
        blocked_path = Path(blocked)

        if normalized == blocked_path:
            return True

        try:
            normalized.relative_to(blocked_path)
            return True
        except ValueError:
            continue

    return False


def validate_path(path):
    """
    Validate a filesystem path before allowing file operations.
    """

    if not path:
        return {
            "allowed": False,
            "reason": "Path cannot be empty"
        }

    try:
        normalized = normalize_path(path)
    except (OSError, RuntimeError):
        return {
            "allowed": False,
            "reason": "Invalid path"
        }

    if is_blocked_path(normalized):
        return {
            "allowed": False,
            "reason": "Access to protected system path is blocked"
        }

    return {
        "allowed": True,
        "path": str(normalized),
        "reason": "Path passed validation"
    }
