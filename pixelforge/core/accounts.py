"""Account security: session validity, lockout, and RBAC."""

_ROLE_ACTIONS = {
    "admin": {"read", "upload", "delete"},
    "editor": {"read", "upload"},
    "viewer": {"read", "delete"},  # BUG (PXF-224): viewers must NOT be able to delete.
}


def session_valid(now, expires_at):
    # BUG (PXF-222): expired sessions are still accepted at the expiry instant.
    # TODO: a session is valid only strictly before it expires.
    return now <= expires_at


def is_locked(failed_attempts, limit):
    # BUG (PXF-223): lockout triggers one attempt too late. TODO: lock at the limit (>=).
    return failed_attempts > limit


def can(role, action):
    return action in _ROLE_ACTIONS.get(role, set())
