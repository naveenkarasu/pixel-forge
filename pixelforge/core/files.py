"""Safe handling of uploaded filenames and their content types."""

_CONTENT_TYPES = {
    "png": "image/png",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "gif": "image/gif",
    "webp": "image/webp",
    "svg": "image/svg+xml",
}


def safe_name(name):
    """Return just the safe basename of an uploaded ``name``.

    Strips any directory components and path-traversal (``../``) so an upload can
    never escape the asset directory; an empty result falls back to ``"asset"``.
    """
    base = name.replace("\\", "/").rstrip("/").rsplit("/", 1)[-1]
    return base or "asset"


def content_type(filename):
    """Map a filename's extension to its MIME type (webp and svg included);
    unknown extensions fall back to ``application/octet-stream``."""
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    return _CONTENT_TYPES.get(ext, "application/octet-stream")
