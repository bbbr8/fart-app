# Ultimate Fart App

This repository contains an intentionally silly yet surprisingly polished demonstration of a FastAPI application serving an interactive web page. The front‑end is a single HTML file that uses the Web Audio API to synthesize realistic fart noises on demand. You can choose between a “Tiny Toot”, a “Mega Blast” or let the app surprise you with a random variant. Every time you click a button the counter updates to track how many farts have been triggered during your session.

The aim of this app isn’t to deploy it in production (please don’t), but to show how a trivial API can deliver a fun and dynamic user experience with very little code.

## Running

1. **Install dependencies** (preferably inside a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

2. **Start the development server**:

   ```bash
   uvicorn main:app --reload
   ```

3. **Open your browser** at [http://localhost:8000](http://localhost:8000) and select a fart style. Leave multiple tabs open to watch the counter increment across each page.

## How it works

The `main.py` module spins up a minimal FastAPI application which serves the static HTML from the `static` directory. All of the user interface and sound synthesis lives in `static/index.html`. The page uses:

- A bit of CSS for a clean, playful design.
- A handful of buttons wired to a `playFart()` function.
- The Web Audio API to create and filter white noise, modulating its tone and duration to mimic different types of farts.
- A counter stored in JavaScript to track how many times the functions have been called.

Because the farts are generated on the fly, there are no sound files to ship and everything runs entirely in your browser.

Feel free to extend the app with additional fart styles, animations or sound effects if you’re feeling especially juvenile.
