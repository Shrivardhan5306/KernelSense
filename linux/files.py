from pathlib import Path

from security.path_validator import validate_path


def get_file_info(file_path):
    """Return information about a file."""

    validation = validate_path(file_path)

    if not validation["allowed"]:
        return {
            "success": False,
            "error": validation["reason"]
        }

    path = Path(validation["path"])

    if not path.exists():
        return {
            "success": False,
            "error": "File or directory does not exist"
        }

    try:
        stat = path.stat()

        return {
            "success": True,
            "name": path.name,
            "path": str(path),
            "size_bytes": stat.st_size,
            "is_file": path.is_file(),
            "is_directory": path.is_dir(),
            "modified_time": stat.st_mtime
        }

    except (PermissionError, OSError) as error:
        return {
            "success": False,
            "error": str(error)
        }


def search_files(directory, filename):
    """Search for files matching a filename."""

    validation = validate_path(directory)

    if not validation["allowed"]:
        return {
            "success": False,
            "error": validation["reason"],
            "results": []
        }

    directory = Path(validation["path"])
    results = []

    if not directory.exists() or not directory.is_dir():
        return {
            "success": False,
            "error": "Directory does not exist",
            "results": []
        }

    try:
        for path in directory.rglob(filename):
            try:
                if path.is_file():
                    results.append(str(path.absolute()))
            except (PermissionError, OSError):
                continue

    except (PermissionError, OSError) as error:
        return {
            "success": False,
            "error": str(error),
            "results": []
        }

    return {
        "success": True,
        "error": None,
        "results": results
    }


def find_large_files(directory, min_size_mb=100):
    """Find files larger than the specified size."""

    validation = validate_path(directory)

    if not validation["allowed"]:
        return {
            "success": False,
            "error": validation["reason"],
            "results": []
        }

    directory = Path(validation["path"])
    results = []

    if not directory.exists() or not directory.is_dir():
        return {
            "success": False,
            "error": "Directory does not exist",
            "results": []
        }

    min_size_bytes = min_size_mb * 1024 * 1024

    try:
        for path in directory.rglob("*"):
            try:
                if path.is_file():
                    size = path.stat().st_size

                    if size >= min_size_bytes:
                        results.append({
                            "name": path.name,
                            "path": str(path.absolute()),
                            "size_bytes": size
                        })

            except (PermissionError, OSError):
                continue

    except (PermissionError, OSError) as error:
        return {
            "success": False,
            "error": str(error),
            "results": []
        }

    results.sort(
        key=lambda file: file["size_bytes"],
        reverse=True
    )

    return {
        "success": True,
        "error": None,
        "results": results
    }


def get_directory_info(directory):
    """Return basic information about a directory."""

    validation = validate_path(directory)

    if not validation["allowed"]:
        return {
            "success": False,
            "error": validation["reason"]
        }

    directory = Path(validation["path"])

    if not directory.exists() or not directory.is_dir():
        return {
            "success": False,
            "error": "Directory does not exist"
        }

    try:
        files = 0
        directories = 0

        for path in directory.iterdir():
            try:
                if path.is_file():
                    files += 1
                elif path.is_dir():
                    directories += 1
            except (PermissionError, OSError):
                continue

        return {
            "success": True,
            "path": str(directory),
            "files": files,
            "directories": directories
        }

    except (PermissionError, OSError) as error:
        return {
            "success": False,
            "error": str(error)
        }
