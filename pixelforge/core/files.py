"""Safe handling of uploaded filenames and their content types."""

_CONTENT_TYPES = {
    "png": "image/png",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "gif": "image/gif",
    # BUG (PXF-212): webp and svg uploads have no content type. TODO: add them.
}


def safe_name(name):
    # BUG (PXF-210): returns the raw name, so `../../etc/passwd` escapes the asset
    # directory. TODO: strip directory components and fall back to "asset".
    return name


def content_type(filename):
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    return _CONTENT_TYPES.get(ext, "application/octet-stream")
