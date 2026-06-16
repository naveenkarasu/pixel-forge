"""Storage keys for uploaded assets."""

from pixelforge.core.files import safe_name


def asset_key(studio, filename):
    # BUG (PXF-214): no studio namespace — the same filename in two studios
    # collides in object storage. TODO: namespace the key by studio.
    return safe_name(filename)
