"""
=== Cat Pics command for Kitty Bot
"""
from config.supabase_config import SupabaseClient
from shared.common import *

"""Sends cat memes or pics to the user using the `pics` command"""
class Pic(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name='sendpic', aliases=['sp'])
    async def pic_embed(self, ctx):
        embed = discord.Embed(
            title='cat pic!',
            description='Lorem ipsum'
        )
        embed.set_author(name='Kitty Bot')
        embed.set_image(url='https://scovljeikdvebtlzjtao.supabase.co/storage/v1/object/public/images/cats/1.jpg')
        embed.add_field(name='here\'s a cat pic for you! *meow*', value=ctx.author.mention)
        embed.set_footer(text='Image retrieved from Supabase. Please support Kitty Bot by following the bot author\'s Github page.')

        await ctx.send(content='Embed', embed=embed)

async def setup(bot) -> None:
    await bot.add_cog(Pic(bot))