from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import os
from config import lifespan, IMAGE_PATH, IMAGE_CACHE_TIME
from image_handler import fetch_image


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse)
async def root():
    """Serve the index HTML page."""
    return 'templates/index.html'

@app.get("/image", response_class=FileResponse)
async def get_image():
    """Serve the image, fetching it if necessary."""
    if not os.path.exists(IMAGE_PATH) or (datetime.now() - datetime.fromtimestamp(os.path.getmtime(IMAGE_PATH))) > IMAGE_CACHE_TIME:
        fetch_image()
    return IMAGE_PATH