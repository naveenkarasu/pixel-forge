"""Asset API: list (paginated) and create. In-memory store until the DB tickets."""

from fastapi import APIRouter
from pydantic import BaseModel

from pixelforge.core.files import content_type, safe_name
from pixelforge.core.pagination import paginate
from pixelforge.core.storage import asset_key

router = APIRouter(prefix="/assets", tags=["assets"])

# In-memory store; replaced by SQLModel + Postgres from the database tickets.
_ASSETS: list[dict] = []


class AssetIn(BaseModel):
    studio: str
    filename: str
    size: int


@router.get("")
def list_assets(page: int = 1, size: int = 20):
    return paginate(_ASSETS, page, size)


@router.post("", status_code=201)
def create_asset(asset: AssetIn):
    name = safe_name(asset.filename)
    record = {
        "key": asset_key(asset.studio, name),
        "name": name,
        "content_type": content_type(name),
        "size": asset.size,
    }
    _ASSETS.append(record)
    return record
