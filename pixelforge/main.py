"""Pixel Forge API entrypoint."""

from fastapi import FastAPI

from pixelforge.api import assets, auth

app = FastAPI(title="Pixel Forge", version="0.1.0")
app.include_router(assets.router)
app.include_router(auth.router)


@app.get("/health")
def health():
    return {"status": "ok"}
