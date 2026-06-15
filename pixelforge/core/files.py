"""Safe handling of uploaded filenames."""


def safe_name(name):
    """Return just the safe basename of an uploaded ``name``.

    Strips any directory components and path-traversal (``../``) so an upload can
    never escape the asset directory; an empty result falls back to ``"asset"``.
    """
    base = name.replace("\\", "/").rstrip("/").rsplit("/", 1)[-1]
    return base or "asset"
