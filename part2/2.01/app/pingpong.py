from fastapi import FastAPI

app = FastAPI()
counter = 0

@app.get("/pingpong")
def read_pingpong():
    global counter
    counter += 1
    response = f"pong {counter}"
    return response

@app.get("/pong_count")
def get_pong_count():
    return {"count": counter}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8020)