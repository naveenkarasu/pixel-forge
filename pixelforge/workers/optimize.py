"""Image optimization worker (delivered by Dev)."""


def optimized_size(size_bytes, quality=0.8):
    """Estimate the optimized byte size at a given quality (stub heuristic)."""
    return int(size_bytes * quality)
