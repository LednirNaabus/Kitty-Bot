import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

# ENVIRONMENT VARIABLES
DISCORD_BOT_TOKEN = os.environ["BOT_TOKEN"]
# Supabase configs
url: str = os.environ["SUPABASE_PROJ_URL"]
key: str = os.environ["SUPABASE_API_KEY"]
supabase: Client = create_client(url, key)

# Bot configs
STARTUP_MESSAGE = "Starting Kitty Bot v.1..."
STARTUP_MESSAGE_COMPLETE = "Startup Complete!"

BOT_PREFIX = "!"