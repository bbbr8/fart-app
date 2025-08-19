"""Ultimate Fart App
====================

This module defines a polished FastAPI application that serves a single
static HTML page. The page contains multiple buttons that trigger
synthetic fart sounds via the Web Audio API. The app demonstrates
how a minimal Python API can deliver a surprisingly interactive and
playful experience with no external assets.
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Determine the path to the directory containing this file
base_path = Path(__file__).resolve().parent
static_dir = base_path / "static"

# Mount the static directory so the browser can request /static/* assets if added later
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


@app.get("/", response_class=HTMLResponse)
async def serve() -> HTMLResponse:
    """Return the front page from the static folder."""
    index_file = static_dir / "index.html"
    return HTMLResponse(index_file.read_text(encoding="utf-8"))
