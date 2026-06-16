"""Presigned S3 upload URLs (delivered by Maya)."""

from pixelforge.core.storage import asset_key


def presigned_put_url(studio, filename, base_url="https://assets.pixelforge.dev"):
    """Return a (stub) presigned PUT URL an uploader can use directly."""
    return f"{base_url}/{asset_key(studio, filename)}?signature=stub"
