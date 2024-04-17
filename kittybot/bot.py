import sys
import traceback
import os
from config.supabase_config import SupabaseClient
from shared.common import *
from discord.ext.commands import ExtensionFailed, ExtensionNotFound

extensions = []
# add extensions here
for f in os.listdir('kittybot/cogs'):
    if f.endswith('.py'):
        extensions.append('kittybot.cogs.' + f[:-3])

class KittyBot(commands.Bot):
    def __init__(self, intents=None) -> None:
        if intents is None:
            intents = discord.Intents.default()
            intents.message_content = True
        super().__init__(command_prefix=config.BOT_PREFIX, intents=intents)
        self.add_listener(self.setup_hook)

    async def on_ready(self) -> None:
        print(config.STARTUP_MESSAGE)
        await self.change_presence(
            status = discord.Status.online,
            activity = discord.Game(name="Kitty Bot - type {}help for help commands.".format(config.BOT_PREFIX))
        )
        print(config.STARTUP_MESSAGE_COMPLETE)

    async def setup_hook(self) -> None:
        for extension in extensions:
            try:
                await self.load_extension(extension)
            except(
                ExtensionNotFound,
                ExtensionFailed
            ):
                print(f"Failed to load {extension}.", file = sys.stderr)
                traceback.print_exception()

    def run_bot(self):
        super().run(config.DISCORD_BOT_TOKEN)