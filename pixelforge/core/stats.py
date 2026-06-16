"""Dashboard statistics over a project's assets."""


def storage_total(sizes):
    """Total bytes used across all asset ``sizes`` (counts every asset)."""
    return sum(sizes)


def avg_asset_size(sizes):
    """Average asset size in bytes; an empty project averages 0 (no crash)."""
    if not sizes:
        return 0
    return sum(sizes) // len(sizes)
