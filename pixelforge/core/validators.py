"""Input validators for signup / assets."""

import re

# Accept plus-tagged local parts (team+billing@studio.com) and normal addresses;
# reject obviously malformed ones (missing local part, missing domain, no TLD).
_EMAIL = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")


def is_valid_email(email):
    """Return True if ``email`` is a plausibly valid address (plus-tags allowed)."""
    return bool(_EMAIL.match(email.strip()))
