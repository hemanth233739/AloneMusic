import asyncio
import importlib
from pytgcalls import PyTgCalls
import time
from pyrogram import Client
from Alone import config

# Constants for user IDs
SUDO_USERS = config.SUDO_USERS
OWNER_ID = config.OWNER_ID
BOT_ID = config.BOT_ID
BOT_NAME = ""
BOT_USERNAME = ""
ASSID = config.ASSID
ASSNAME = ""
ASSUSERNAME = ""

# Initialize clients
smexy = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(smexy)

app = Client(
    "Alone",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

client = Client(
    "Alone",
    config.API_ID,
    config.API_HASH,
    session_string=config.SESSION_NAME
)

def all_info(app, client):
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID, ASSNAME, ASSUSERNAME

    # Use await with async function
    getme = app.get_me()  # Ensure this is awaited
    getme1 = client.get_me()  # Ensure this is awaited

    BOT_ID = getme.id
    ASSID = getme1.id
    BOT_NAME = getme.first_name + (" " + getme.last_name if getme.last_name else "")
    BOT_USERNAME = getme.username
    ASSNAME = getme1.first_name + (" " + getme1.last_name if getme1.last_name else "")
    ASSUSERNAME = getme1.username

# Start the clients and gather information
async def main():
    await app.start()
    await client.start()
    await all_info(app, client)

# Run the asyncio main function
if __name__ == "__main__":
    asyncio.run(main())

