"""Session model (delivered by Priya)."""

from sqlmodel import Field, SQLModel


class Session(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    account_id: int
    token: str
    expires_at: int
