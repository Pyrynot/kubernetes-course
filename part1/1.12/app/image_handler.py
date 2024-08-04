import httpx
from fastapi import HTTPException
from config import IMAGE_URL, IMAGE_PATH
import logging

logging.basicConfig(level=logging.INFO)

def fetch_image():
    try:
        logging.info(f"Fetching image from {IMAGE_URL}")
        response = httpx.get(IMAGE_URL, follow_redirects=True)
        if response.status_code != 200:
            logging.error(f"Failed to fetch image. Status code: {response.status_code}")
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch image")
        
        content = response.content
        with open(IMAGE_PATH, 'wb') as f:
            f.write(content)
        logging.info(f"Image saved to {IMAGE_PATH}")
    except httpx.RequestError as e:
        logging.error(f"An error occurred while requesting the image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred while requesting the image: {str(e)}")