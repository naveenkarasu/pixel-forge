"""Human-readable asset sizes for the studio dashboard."""


def humansize(n):
    # BUG (PXF-213): always reports raw bytes. TODO: scale to KB/MB/GB/...
    return f"{n} B"
