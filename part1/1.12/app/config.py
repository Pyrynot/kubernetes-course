from datetime import timedelta
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    port = os.getenv('PORT')
    print(f"Server started on port {port}")
    yield
    print("Server is shutting down")

IMAGE_URL = "https://picsum.photos/1200"
IMAGE_PATH = "/app/static/image.jpg"
IMAGE_CACHE_TIME = timedelta(seconds=15)
