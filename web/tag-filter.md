# Dashboard: tag filter (delivered by Raj)

The studio dashboard's asset grid gains a tag filter chip-row. Selecting tags
calls `GET /assets?tags=art,sprite`; the backend filters with the normalized,
de-duplicated tag set (see `core/tags.py`).

> Frontend stub for the curriculum — the real React component lives in the
> dashboard app; this note marks Raj's delivery in the timeline.
