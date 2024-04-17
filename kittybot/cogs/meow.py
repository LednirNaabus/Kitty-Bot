"""
=== MEOW commands for Kitty Bot ===
1. Happy meow
2. Sad meow
3. Angry meow
4. Cute meow
5. Sleepy meow
"""
from shared.common import *
from io import BytesIO
import asyncio

"""Greets users with meow"""
class Meow(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self._last_member = None

    # Happy meow
    @commands.command(aliases=['mh'])
    async def happy_meow(self, ctx, *, member: discord.Member = None):
        # args = ctx.message.content.split()
        member = member or ctx.author

        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Meow. {member.name}~~ *purr*')
        else:
            await ctx.send(f'Meow! {member.name} :)')
        self._last_member = member

    # Sad meow
    @commands.command(aliases=['ms'])
    async def sad_meow(self, ctx, *, member: discord.Member = None):
        # args = ctx.message.content.split()
        member = member or ctx.author

        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Meow. {member.name}~~ *purr*')
        else:
            await ctx.send(f'Meow... {member.name} :(')
        self._last_member = member

    # Angry meow
    @commands.command(aliases=['ma'])
    async def angry_meow(self, ctx, *, member: discord.Member = None):
        # args = ctx.message.content.split()
        member = member or ctx.author

        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Meow. {member.name}~~ *purr*')
        else:
            await ctx.send(f'Meow!!! *hiss* {member.name} >:(')
        self._last_member = member

    # Cute meow
    @commands.command(aliases=['mc'])
    async def cute_meow(self, ctx, *, member: discord.Member = None):
        # args = ctx.message.content.split()
        member = member or ctx.author

        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Meow. {member.name}~~ *purr*')
        else:
            await ctx.send(f'Meow! :3 {member.name} uwu')
        self._last_member = member

    # Sleepy meow
    @commands.command(aliases=['mzzz'])
    async def sleepy_meow(self, ctx, *, member: discord.Member = None):
        # args = ctx.message.content.split()
        member = member or ctx.author

        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Meow. {member.name}~~ *purr*')
        else:
            await ctx.send(f'Meow... {member.name} zzz')
        self._last_member = member


async def setup(bot) -> None:
    await bot.add_cog(Meow(bot))