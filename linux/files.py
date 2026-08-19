from pathlib import Path


def get_file_info(file_path):
    """Return information about a file."""
    path = Path(file_path)

    if not path.exists():
        return None

    try:
        stat = path.stat()

        return {
            "name": path.name,
            "path": str(path.absolute()),
            "size_bytes": stat.st_size,
            "is_file": path.is_file(),
            "is_directory": path.is_dir(),
            "modified_time": stat.st_mtime
        }

    except (PermissionError, OSError):
        return None


def search_files(directory, filename):
    """Search for files matching a filename."""
    directory = Path(directory)
    results = []

    if not directory.exists() or not directory.is_dir():
        return results

    try:
        for path in directory.rglob(filename):
            try:
                if path.is_file():
                    results.append(str(path.absolute()))
            except (PermissionError, OSError):
                continue

    except (PermissionError, OSError):
        pass

    return results


def find_large_files(directory, min_size_mb=100):
    """Find files larger than the specified size."""
    directory = Path(directory)
    results = []

    if not directory.exists() or not directory.is_dir():
        return results

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

    except (PermissionError, OSError):
        pass

    results.sort(
        key=lambda file: file["size_bytes"],
        reverse=True
    )

    return results


def get_directory_info(directory):
    """Return basic information about a directory."""
    directory = Path(directory)

    if not directory.exists() or not directory.is_dir():
        return None

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
            "path": str(directory.absolute()),
            "files": files,
            "directories": directories
        }

    except (PermissionError, OSError):
        return None
