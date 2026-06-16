"""Audit-log helpers."""


def mask_email(email):
    """Mask the local part for audit logs: ``john@x.com`` -> ``j***@x.com``."""
    local, sep, domain = email.partition("@")
    if not sep:
        return "***"
    masked = (local[0] + "***") if local else "***"
    return f"{masked}@{domain}"
