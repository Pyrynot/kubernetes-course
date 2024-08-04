from datetime import datetime
import time
import hashlib
import httpx
from fastapi import FastAPI
import asyncio
from contextlib import asynccontextmanager

PINGPONG_SERVICE_URL = "http://pingponglog-svc:8020/pong_count"
log = ""


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(log_output())
    yield
    task.cancel()
    await task
    print("Server is shutting down")

app = FastAPI(lifespan=lifespan)


async def log_output():
    global log
    while True:
        current_timestamp = datetime.now().isoformat()
        hash_value = hashlib.sha256(current_timestamp.encode()).hexdigest()
        try:
            response = httpx.get(PINGPONG_SERVICE_URL)
            pong_count = response.json().get("count", "N/A")
            log_entry = f"{current_timestamp}: {hash_value}. Ping / Pongs: {pong_count}"
            log = log_entry
            print(log_entry)
        except httpx.RequestException as e:
            log_entry = f"{current_timestamp}: {hash_value}. Error connecting to pingpong service: {e}"
            log = log_entry
            print(log_entry)
        await asyncio.sleep(5)


@app.get("/latest_log")
def latest_log():
    global log
    if log:
        return {"log": log}
    return {"log": "No logs available"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)