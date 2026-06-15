"""Pagination for the asset-list API (1-indexed pages)."""


def paginate(items, page, size):
    """Return the slice of ``items`` on the 1-indexed ``page`` of ``size`` rows.

    Page 1 starts at index 0 (not ``size``); the last page may be partial.
    """
    if page < 1 or size < 1:
        raise ValueError("page and size must be >= 1")
    start = (page - 1) * size
    return items[start:start + size]
