"""
=== Cat Pics command for Kitty Bot
"""
from config.supabase_config import SupabaseClient
from shared.common import *
import random

"""Sends cat memes or pics to the user using the `pics` command"""
class Pic(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.SupabaseClient = SupabaseClient.get_instance()

    @commands.command(name='sendpic', aliases=['sp'])
    async def pic_embed(self, ctx):
        embed = discord.Embed(
            title='random cat pic!',
            description='Kitty Bot sends you a random cat pic from their phone... *meow*'
        )
        embed.set_author(name='Kitty Bot')
        embed.set_image(url=self.get_random_catpics())
        embed.add_field(name='here\'s a cat pic for you! *meow*', value=ctx.author.mention)
        embed.set_footer(text='Image retrieved from Supabase. Please support Kitty Bot by following the bot author\'s Github page.')

        await ctx.send(embed=embed)
    
    def get_random_catpics(self) -> str:
        supabase_instance = self.SupabaseClient
        response = supabase_instance.table('cat_pics').select('image_url').execute()
        cat_pics = response.data
        get_random_data = random.choice(cat_pics)
        random_pic_url = get_random_data.get('image_url')
        return random_pic_url

async def setup(bot) -> None:
    await bot.add_cog(Pic(bot))