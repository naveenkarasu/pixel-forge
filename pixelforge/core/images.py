"""Thumbnail sizing that preserves aspect ratio."""


def thumb_size(width, height, max_side):
    # BUG (PXF-211): squashes every image to a square, ignoring aspect ratio.
    # TODO: scale to fit within max_side on the longest edge, preserving ratio.
    return (max_side, max_side)
