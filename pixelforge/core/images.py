"""Thumbnail sizing that preserves aspect ratio."""


def thumb_size(width, height, max_side):
    """Scale ``(width, height)`` to fit within ``max_side`` on the longest edge,
    preserving aspect ratio. Images already within bounds are left unchanged
    (no upscaling)."""
    if width <= 0 or height <= 0 or max_side <= 0:
        raise ValueError("dimensions must be positive")
    if width <= max_side and height <= max_side:
        return (width, height)
    scale = max_side / (width if width >= height else height)
    return (round(width * scale), round(height * scale))
