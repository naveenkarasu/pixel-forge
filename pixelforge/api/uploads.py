"""Asset upload endpoint (delivered by Maya)."""

from fastapi import APIRouter
from pydantic import BaseModel

from pixelforge.core.files import content_type, safe_name
from pixelforge.core.storage import asset_key

router = APIRouter(prefix="/uploads", tags=["uploads"])


class UploadIn(BaseModel):
    studio: str
    filename: str


@router.post("", status_code=201)
def create_upload(body: UploadIn):
    name = safe_name(body.filename)
    return {"key": asset_key(body.studio, name), "content_type": content_type(name)}
