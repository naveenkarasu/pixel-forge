"""Account model (delivered by Priya)."""

from sqlmodel import Field, SQLModel


class Account(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str
    password_hash: str
    role: str = "viewer"
    failed_attempts: int = 0
