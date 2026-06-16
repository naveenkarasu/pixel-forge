"""Account security: session validity, lockout, and RBAC."""

_ROLE_ACTIONS = {
    "admin": {"read", "upload", "delete"},
    "editor": {"read", "upload"},
    "viewer": {"read"},
}


def session_valid(now, expires_at):
    """A session is valid only strictly before it expires."""
    return now < expires_at


def is_locked(failed_attempts, limit):
    """An account locks once failed attempts reach the limit (>=, not >)."""
    return failed_attempts >= limit


def can(role, action):
    """RBAC check: viewers may read but never upload/delete."""
    return action in _ROLE_ACTIONS.get(role, set())
