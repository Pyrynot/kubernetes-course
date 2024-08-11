# Commands used:


Staging namespace:

![alt text](image-1.png)


![alt text](image.png)


Depploying to staging on push to the main branch:
![alt text](image-4.png)

Deploying to production with a tag push:
![alt text](image-5.png)

Broadcaster not forwarding messages in staging was achieved with an env variable in prod:

```Python
STAGING_ENV = os.getenv("STAGING_ENV", True)
..........
if message:
    logger.info(f"Sending message to Discord: {message}")
    if not STAGING_ENV:
        await send_to_discord(message)
```