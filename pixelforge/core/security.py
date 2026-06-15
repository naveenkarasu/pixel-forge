"""Auth/security helpers: passwords, sessions, lockout, RBAC, audit masking."""

_ROLE_ACTIONS = {
    "admin": {"read", "upload", "delete"},
    "editor": {"read", "upload"},
    "viewer": {"read"},
}


def is_strong(password):
    """A password is strong with >= 8 chars AND at least one letter AND one digit."""
    return (
        len(password) >= 8
        and any(c.isalpha() for c in password)
        and any(c.isdigit() for c in password)
    )


def session_valid(now, expires_at):
    """A session is valid only strictly before it expires."""
    return now < expires_at


def is_locked(failed_attempts, limit):
    """An account locks once failed attempts reach the limit (>=, not >)."""
    return failed_attempts >= limit


def can(role, action):
    """RBAC check: viewers may read but never upload/delete."""
    return action in _ROLE_ACTIONS.get(role, set())


def mask_email(email):
    """Mask the local part for audit logs: ``john@x.com`` -> ``j***@x.com``."""
    local, sep, domain = email.partition("@")
    if not sep:
        return "***"
    masked = (local[0] + "***") if local else "***"
    return f"{masked}@{domain}"
