# Fart App

This repository contains a tiny demonstration of serving a static
HTML page with FastAPI. The page includes a button that triggers a
simple sound effect via the Web Audio API. It’s a lighthearted test
application designed to verify that your development environment is
working.

## Running

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

3. Open your browser at [`http://localhost:8000`](http://localhost:8000) and click the button to play the sound.
