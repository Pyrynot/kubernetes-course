from contextlib import asynccontextmanager
from fastapi import FastAPI
import os

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    port = os.getenv('PORT', '8000') 
    print(f"Server started on port {port}")
    yield
    print("Server is shutting down")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}