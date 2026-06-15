"""Storage keys for uploaded assets."""

from pixelforge.core.files import safe_name


def asset_key(studio, filename):
    """Namespace an asset by studio so the same filename in two studios never
    collides in object storage."""
    return f"{studio}/{safe_name(filename)}"
