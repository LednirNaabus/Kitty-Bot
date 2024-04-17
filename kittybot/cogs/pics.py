"""
=== Cat Pics command for Kitty Bot
"""
from shared.common import *

"""Sends cat memes or pics to the user using the `pics` command"""
class Pic(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

async def setup(bot) -> None:
    await bot.add_cog(Pic(bot))