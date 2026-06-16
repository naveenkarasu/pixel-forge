"""Human-readable asset sizes for the studio dashboard."""

_UNITS = ("B", "KB", "MB", "GB", "TB", "PB")


def humansize(n):
    """Format a byte count as a human-readable size.

    Bytes render as a whole number (``500 B``); larger units render with one
    decimal place (``1536 -> "1.5 KB"``).
    """
    size = float(n)
    for unit in _UNITS:
        if size < 1024 or unit == _UNITS[-1]:
            if unit == "B":
                return f"{int(size)} {unit}"
            return f"{size:.1f} {unit}"
        size /= 1024
