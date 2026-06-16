"""Dashboard statistics over a project's assets."""


def storage_total(sizes):
    """Total bytes used across all asset ``sizes``."""
    # BUG (PXF-204): drops the last asset. TODO: count every asset.
    return sum(sizes[:-1])


def avg_asset_size(sizes):
    """Average asset size in bytes."""
    # BUG (PXF-205): crashes for an empty project. TODO: handle the empty case.
    return sum(sizes) // len(sizes)
