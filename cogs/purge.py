import discord, aiohttp, io
from discord.ext import commands
from module import *

GLOBAL = 0x03d692

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    @isbanned()
    async def purge(self, ctx, limit: int):
        print("Purge")
        deleted = await ctx.channel.purge(limit=limit)
        em=discord.Embed(title=f'{len(deleted)} Messages Purged!', color=GLOBAL)
        await ctx.send(embed=em)
        await ctx.message.delete()

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont have permission to do that!")

def setup(bot):
    bot.add_cog(Purge(bot))