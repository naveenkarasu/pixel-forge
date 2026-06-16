"""Slugify project / asset names for use in asset URLs."""

import re

_NON_SLUG = re.compile(r"[^a-z0-9]+")


def slugify(title):
    """Lower-case ``title`` and collapse runs of non-alphanumerics into single
    hyphens, trimming leading/trailing hyphens. ``"My Cool Project!" -> "my-cool-project"``.
    """
    return _NON_SLUG.sub("-", title.strip().lower()).strip("-")
