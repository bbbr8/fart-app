"""Fart App
===========

This module defines a very small FastAPI application that serves a static
HTML page. The page contains a single button that triggers a sound
effect via the Web Audio API. While intentionally silly, it
demonstrates serving static content alongside a Python API.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def serve() -> HTMLResponse:
    """Return the front page from the static folder."""
    with open("static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())
