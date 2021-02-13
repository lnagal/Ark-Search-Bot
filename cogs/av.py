import discord, aiohttp, io, json
from discord.ext import commands
from module import *

GLOBAL = 0x03d692

class Av(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pfp', 'avatar'])
    @isbanned()
    async def av(self, ctx, *, user: discord.Member=None): # b'\xfc'
        print("Av")
        format = "gif"
        user = user or ctx.author
        if user.is_avatar_animated() != True:
            format = "png"
        avatar = user.avatar_url_as(format = format if format != "gif" else None)
        async with aiohttp.ClientSession() as session:
            async with session.get(str(avatar)) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file = discord.File(file, f"Avatar.{format}"))    

def setup(bot):
    bot.add_cog(Av(bot))