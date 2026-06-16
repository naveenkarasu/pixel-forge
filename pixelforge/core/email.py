"""Email normalization for login (case-insensitive, trimmed)."""


def normalize_email(email):
    """Lower-case and strip an email so logins are case-insensitive."""
    return email.strip().lower()
