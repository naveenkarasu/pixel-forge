"""Slugify project / asset names for use in asset URLs."""


def slugify(title):
    # BUG (PXF-203): only lower-cases and swaps spaces — leaves punctuation in and
    # doesn't trim. TODO: collapse non-alphanumerics to single hyphens and trim.
    return title.lower().replace(" ", "-")
