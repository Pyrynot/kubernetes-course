from fastapi import FastAPI
from contextlib import asynccontextmanager

app = FastAPI()
counter = 0

file_path = "/mnt/data/counter.txt"

@asynccontextmanager
async def lifespan(app: FastAPI):
    global counter
    try:
        with open(file_path, "r") as file:
            counter = int(file.read())
    except FileNotFoundError:
        pass
    yield
    print("Server is shutting down")

@app.get("/pingpong")
def read_pingpong():
    global counter
    response = f"pong {counter}"
    counter += 1
    with open(file_path, "w") as file:
        file.write(str(counter))
    return response

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8020)