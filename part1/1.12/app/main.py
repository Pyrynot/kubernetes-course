from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import os
from config import lifespan, IMAGE_PATH, IMAGE_CACHE_TIME
from image_handler import fetch_image


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse('templates/index.html')

@app.get("/image")
async def get_image():
    if not os.path.exists(IMAGE_PATH) or (datetime.now() - datetime.fromtimestamp(os.path.getmtime(IMAGE_PATH))) > IMAGE_CACHE_TIME:
        fetch_image()
    return FileResponse(IMAGE_PATH)