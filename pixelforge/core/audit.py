"""Audit-log helpers."""


def mask_email(email):
    # BUG (PXF-225): logs the raw email. TODO: mask the local part (j***@x.com).
    return email
