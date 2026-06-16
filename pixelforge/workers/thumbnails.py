"""Thumbnail worker (delivered by Dev)."""

from pixelforge.core.images import thumb_size


def make_thumbnail(width, height, max_side=256):
    """Return the (w, h) of the thumbnail generated for a source image."""
    return thumb_size(width, height, max_side)
