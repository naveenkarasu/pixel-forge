"""Input validators for signup / assets."""


def is_valid_email(email):
    # BUG (PXF-202): too loose — accepts anything containing '@', so `bad@` and
    # `@studio.com` slip through. TODO: require a local part, a domain, and a TLD
    # (while still allowing plus-tags).
    return "@" in email
