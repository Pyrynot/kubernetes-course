from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    port = os.getenv('PORT') 
    print(f"Server started on port {port}")
    yield
    print("Server is shutting down")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return FileResponse('templates/index.html')