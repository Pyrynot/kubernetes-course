
from fastapi import FastAPI
import time

log_file_path = "/shared/log.txt"

def read_log():
    retries = 10
    for _ in range(retries):
        try:
            with open(log_file_path, "r") as file:
                content = file.read().strip()
            return content
        except FileNotFoundError:
            time.sleep(0.1)


app = FastAPI()

@app.get("/")
def get_status():
    return read_log()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
