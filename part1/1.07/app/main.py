import uuid
from datetime import datetime
from fastapi import FastAPI
import asyncio
from pydantic import BaseModel
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(logger.log_output())
    yield
    print("Server is shutting down")

app = FastAPI(lifespan=lifespan)

class Status(BaseModel):
    timestamp: str
    random_string: str

class Logger:
    def __init__(self) -> None:
        self.current_timestamp = None
        self.current_string = str(uuid.uuid4())

    async def log_output(self):
        while True:
            self.current_timestamp = datetime.now().isoformat()
            print(f"{self.current_timestamp}: {self.current_string}")
            await asyncio.sleep(5)

    def get_status(self):
        return Status(timestamp=self.current_timestamp, random_string=self.current_string)

logger = Logger()

@app.get("/status", response_model=Status)
def get_status():
    return logger.get_status()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)