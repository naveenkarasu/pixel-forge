"""Visible tests for the auth/accounts helpers."""

from pixelforge.core.email import normalize_email
from pixelforge.core.security import (
    can,
    is_locked,
    is_strong,
    mask_email,
    session_valid,
)
from pixelforge.core.validators import is_valid_email


def test_is_valid_email_accepts_plus_tags():
    assert is_valid_email("team+billing@studio.com")
    assert is_valid_email("a@b.co")
    assert not is_valid_email("bad@")
    assert not is_valid_email("@studio.com")
    assert not is_valid_email("nope")


def test_normalize_email():
    assert normalize_email("  John@Studio.COM ") == "john@studio.com"


def test_is_strong():
    assert is_strong("abc12345")
    assert not is_strong("short1")        # too short
    assert not is_strong("allletters")    # no digit
    assert not is_strong("12345678")      # no letter


def test_session_valid():
    assert session_valid(5, 10)
    assert not session_valid(10, 10)      # expiry is exclusive
    assert not session_valid(11, 10)


def test_is_locked():
    assert is_locked(5, 5)                # locks AT the limit
    assert is_locked(6, 5)
    assert not is_locked(4, 5)


def test_rbac_can():
    assert can("admin", "delete")
    assert can("editor", "upload")
    assert not can("viewer", "delete")
    assert can("viewer", "read")
    assert not can("ghost", "read")


def test_mask_email():
    assert mask_email("john@example.com") == "j***@example.com"
    assert mask_email("a@x.com") == "a***@x.com"
    assert mask_email("notanemail") == "***"
