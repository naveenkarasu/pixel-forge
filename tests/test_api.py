"""Visible tests for the FastAPI app (boots, validates, paginates)."""

from fastapi.testclient import TestClient

from pixelforge.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_signup_validation():
    ok = client.post("/auth/signup", json={"email": "team+x@studio.com", "password": "abc12345"})
    assert ok.status_code == 201
    assert ok.json() == {"email": "team+x@studio.com"}
    assert client.post("/auth/signup", json={"email": "bad@", "password": "abc12345"}).status_code == 422
    assert client.post("/auth/signup", json={"email": "a@b.co", "password": "weak"}).status_code == 422


def test_assets_create_and_paginate():
    for i in range(5):
        r = client.post("/assets", json={"studio": "s1", "filename": f"../{i}.png", "size": 100})
        assert r.status_code == 201
    page1 = client.get("/assets", params={"page": 1, "size": 2}).json()
    assert len(page1) == 2
    assert page1[0]["content_type"] == "image/png"
    assert page1[0]["key"].startswith("s1/")
