"""Pagination for the asset-list API (1-indexed pages)."""


def paginate(items, page, size):
    """Return the slice of ``items`` on the 1-indexed ``page`` of ``size`` rows."""
    # BUG (PXF-201): page 1 starts at index `size` instead of 0, so every page
    # loses its first item. TODO: fix the start index for 1-indexed pages.
    start = page * size
    return items[start:start + size]
