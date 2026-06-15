"""Auth API: studio signup with email + password validation."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from pixelforge.core.email import normalize_email
from pixelforge.core.security import is_strong
from pixelforge.core.validators import is_valid_email

router = APIRouter(prefix="/auth", tags=["auth"])


class SignupIn(BaseModel):
    email: str
    password: str


@router.post("/signup", status_code=201)
def signup(body: SignupIn):
    if not is_valid_email(body.email):
        raise HTTPException(status_code=422, detail="invalid email")
    if not is_strong(body.password):
        raise HTTPException(status_code=422, detail="weak password")
    return {"email": normalize_email(body.email)}
