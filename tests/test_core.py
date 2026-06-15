"""Visible unit tests for the core helpers (you run these yourself)."""

from pixelforge.core.files import safe_name
from pixelforge.core.humansize import humansize
from pixelforge.core.pagination import paginate
from pixelforge.core.slug import slugify


def test_paginate_is_one_indexed():
    items = list(range(1, 11))
    assert paginate(items, 1, 3) == [1, 2, 3]
    assert paginate(items, 2, 3) == [4, 5, 6]
    assert paginate(items, 4, 3) == [10]  # partial last page


def test_slugify():
    assert slugify("My Cool Project!") == "my-cool-project"
    assert slugify("  Hello   World  ") == "hello-world"
    assert slugify("already-slug") == "already-slug"


def test_humansize():
    assert humansize(500) == "500 B"
    assert humansize(1536) == "1.5 KB"
    assert humansize(5 * 1024 * 1024) == "5.0 MB"


def test_safe_name():
    assert safe_name("../../etc/passwd") == "passwd"
    assert safe_name("a/b/c.jpg") == "c.jpg"
    assert safe_name("logo.png") == "logo.png"
    assert safe_name("") == "asset"
