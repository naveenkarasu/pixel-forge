"""Asset tag normalization and de-duplication."""


def normalize_tag(tag):
    """Lower-case and trim a single tag."""
    return tag.strip().lower()


def dedupe_tags(tags):
    """Remove duplicate tags, preserving first-seen order."""
    seen = set()
    out = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def normalize_tags(tags):
    """Normalize each tag, drop blanks, and de-duplicate (order-preserving)."""
    return dedupe_tags([n for n in (normalize_tag(t) for t in tags) if n])
