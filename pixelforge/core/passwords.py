"""Password strength check (signup)."""


def is_strong(password):
    """Strong = >= 8 chars AND at least one letter AND one digit."""
    return (
        len(password) >= 8
        and any(c.isalpha() for c in password)
        and any(c.isdigit() for c in password)
    )
