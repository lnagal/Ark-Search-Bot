import discord, json, random, typing
from discord.ext import commands
from module import *

GLOBAL = 0x03d692

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["em"])
    @commands.has_permissions(administrator=True)
    @isbanned()
    async def embed(self, ctx, color: typing.Optional[discord.Color] = None, *, text):
        print("Embed")
        em = discord.Embed(color=GLOBAL)
        em.description = text
        await ctx.send(embed=em)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Embed(bot))