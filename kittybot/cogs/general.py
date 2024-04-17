"""
=== GENERAL BOT COMMANDS ===
"""
from shared.common import *

class General(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Cog_{}: {}".format(General.__name__, config.STARTUP_MESSAGE))
        print("Cog_{}: {}".format(General.__name__, config.STARTUP_MESSAGE_COMPLETE))

        # basic commands here i.e. help, utility commands

async def setup(bot) -> None:
    await bot.add_cog(General(bot))