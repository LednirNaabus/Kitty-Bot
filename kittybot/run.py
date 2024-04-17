import asyncio
from kittybot.bot import KittyBot
from config import config

def run():
    bot = KittyBot()
    asyncio.run(bot.run_bot())

if __name__ == "__main__":
    if config.DISCORD_BOT_TOKEN == "":
        print("No token found.")
        exit
    else:
        run()