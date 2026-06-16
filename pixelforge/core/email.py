"""Email normalization for login (case-insensitive, trimmed)."""


def normalize_email(email):
    # BUG (PXF-220): no normalization, so logins are case-sensitive. TODO: lower + strip.
    return email
