from fastapi import FastAPI
import httpx

LOGGER_SERVICE_URL = "http://logoutput-svc:8000/latest_log"

app = FastAPI()

@app.get("/")
def get_status():
    try:
        response = httpx.get(LOGGER_SERVICE_URL)
        return response.json()
    except httpx.RequestError as e:
        return {"error": f"Error connecting to logger service: {e}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
