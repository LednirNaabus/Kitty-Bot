"""
=== MEOW commands for Kitty Bot ===
1. Happy meow
2. Sad meow
3. Angry meow
4. Cute meow
5. Sleepy meow
"""
from shared.common import *

"""Greets users with meow"""
class Meow(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.emotion = {
            "happy_face": "\U0001F63A",
            "sad_face": "\U0001F63F",
            "angry_face": "\U0001F63E",
            "cute_face": "\U0001F97A",
            "sleepy_face": "\U0001F634"
        }

    # Happy meow
    @commands.command(name='happymeow', aliases=['mh'])
    async def happy_meow(self, ctx):
        await ctx.send(f'meow! *purr*... {ctx.author} {self.emotion["happy_face"]}')

    # Sad meow
    @commands.command(name='sadmeow', aliases=['ms'])
    async def sad_meow(self, ctx):
        await ctx.send(f'meow... {ctx.author} {self.emotion["sad_face"]}')

    # Angry meow
    @commands.command(name='hiss', aliases=['ma'])
    async def angry_meow(self, ctx):
        await ctx.send(f'meow!!! *hiss* {ctx.author} {self.emotion["angry_face"]}')

    # Cute Meow
    @commands.command(name='cutemeow', aliases=['mc'])
    async def cute_meow(self, ctx):
        await ctx.send(f'meow! uwu {ctx.author} {self.emotion["cute_face"]}')

    # Sleepy Meow
    @commands.command(name='sleepymeow', aliases=['mzzz'])
    async def sleepy_meow(self, ctx):
        await ctx.send(f'meow... zzz {ctx.author} {self.emotion["sleepy_face"]}')

async def setup(bot) -> None:
    await bot.add_cog(Meow(bot))