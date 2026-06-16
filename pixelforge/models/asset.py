"""Asset model (delivered by Priya)."""

from sqlmodel import Field, SQLModel


class Asset(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    studio: str
    key: str
    content_type: str
    size: int
