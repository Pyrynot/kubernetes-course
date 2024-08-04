from datetime import timedelta
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from typing import AsyncGenerator

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Context manager for the app lifespan."""
    port = os.getenv('PORT', '8000')
    print(f"Server started on port {port}")
    yield
    print("Server is shutting down")

IMAGE_URL = "https://picsum.photos/1200"
IMAGE_PATH = "./static/image.jpg"
IMAGE_CACHE_TIME = timedelta(hours=1)
