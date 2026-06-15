"""Visible tests for the asset-pipeline helpers."""

from pixelforge.core.files import content_type
from pixelforge.core.images import thumb_size
from pixelforge.core.stats import avg_asset_size, storage_total
from pixelforge.core.storage import asset_key
from pixelforge.core.tags import dedupe_tags, normalize_tags


def test_storage_total_counts_every_asset():
    assert storage_total([10, 20, 30]) == 60
    assert storage_total([]) == 0


def test_avg_asset_size_handles_empty():
    assert avg_asset_size([]) == 0
    assert avg_asset_size([10, 20, 30]) == 20


def test_dedupe_tags_keeps_order():
    assert dedupe_tags(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]


def test_normalize_tags():
    assert normalize_tags([" Art ", "art", "PIXEL", "  "]) == ["art", "pixel"]


def test_thumb_size_preserves_aspect():
    assert thumb_size(400, 200, 100) == (100, 50)
    assert thumb_size(200, 400, 100) == (50, 100)
    assert thumb_size(50, 50, 100) == (50, 50)  # no upscaling


def test_content_type():
    assert content_type("a.webp") == "image/webp"
    assert content_type("logo.SVG") == "image/svg+xml"
    assert content_type("x.png") == "image/png"
    assert content_type("noext") == "application/octet-stream"


def test_asset_key_namespaces_by_studio():
    assert asset_key("studio-a", "logo.png") == "studio-a/logo.png"
    assert asset_key("s1", "x.png") != asset_key("s2", "x.png")
    assert asset_key("s", "../../etc/passwd") == "s/passwd"
