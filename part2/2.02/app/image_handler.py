import httpx
from fastapi import HTTPException
from config import IMAGE_URL, IMAGE_PATH
import logging
import os

logging.basicConfig(level=logging.INFO)


def fetch_image() -> None:
    """Fetch and save the image from the specified URL."""
    try:
        logging.info(f"Fetching image from {IMAGE_URL}")
        response = httpx.get(IMAGE_URL, follow_redirects=True)
        response.raise_for_status()

        os.makedirs(os.path.dirname(IMAGE_PATH), exist_ok=True)
        
        with open(IMAGE_PATH, 'wb') as f:
            f.write(response.content)
        
        logging.info(f"Image saved to {IMAGE_PATH}")
    except httpx.RequestError as e:
        logging.error(f"An error occurred while requesting the image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred while requesting the image: {str(e)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred while fetching the image.")