"""Asset tag normalization and de-duplication."""


def normalize_tag(tag):
    return tag.strip().lower()


def dedupe_tags(tags):
    # BUG (PXF-206): doesn't actually remove duplicates. TODO: drop repeats while
    # preserving first-seen order.
    return list(tags)


def normalize_tags(tags):
    return dedupe_tags([n for n in (normalize_tag(t) for t in tags) if n])
