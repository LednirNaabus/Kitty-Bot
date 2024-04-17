import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.environ["BOT_TOKEN"]

# Bot configs
STARTUP_MESSAGE = "Starting Kitty Bot v.1..."
STARTUP_MESSAGE_COMPLETE = "Startup Complete!"

BOT_PREFIX = "!"