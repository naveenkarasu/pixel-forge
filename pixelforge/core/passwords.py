"""Password strength check (signup)."""


def is_strong(password):
    # BUG (PXF-221): only checks length. TODO: also require at least one letter
    # AND one digit.
    return len(password) >= 8
