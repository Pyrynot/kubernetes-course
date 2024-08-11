import os
import json
import asyncio
import nats
import httpx
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
NATS_URL = os.getenv("NATS_URL")
STAGING_ENV = os.getenv("STAGING_ENV", True)

async def send_to_discord(message: str):
    async with httpx.AsyncClient() as client:
        payload = {"content": message}
        response = await client.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()

async def message_handler(msg):
    data = json.loads(msg.data.decode('utf-8'))
    event = data.get("event")
    todo = data.get("data")

    if event == "todo_created":
        message = f"A new todo was created: {todo['content']}"
    elif event == "todo_updated":
        message = f"Todo updated: {todo['content']} - Done: {todo['done']}"

    if message:
        logger.info(f"Sending message to Discord: {message}")
        if not STAGING_ENV:
            await send_to_discord(message)

async def run():
    logger.info("Starting broadcaster...")
    try:
        nc = await nats.connect(NATS_URL)
        logger.info(f"Connected to NATS at {NATS_URL}")
        await nc.subscribe("todos.events", "broadcaster-group", cb=message_handler)
        logger.info("Subscribed to 'todos.events' topic with queue group 'broadcaster-group'.")
    except Exception as e:
        logger.error(f"Failed to connect to NATS: {str(e)}")
        return

    logger.info("Broadcaster is running...")
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(run())
