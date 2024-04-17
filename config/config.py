import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

# ENVIRONMENT VARIABLES
DISCORD_BOT_TOKEN = os.environ["BOT_TOKEN"]

# Bot configs
STARTUP_MESSAGE = "Starting Kitty Bot v.1..."
STARTUP_MESSAGE_COMPLETE = "Startup Complete!"

BOT_PREFIX = "!"