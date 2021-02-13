import discord, asyncio
from discord.ext import commands
from module import *

GLOBAL = 0x03d692

class Nigga(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nigga")
    @isbanned()
    async def nigga(self, ctx):
        print("Nigga")
        await ctx.send('Watup nigga how you doing today?')
        await asyncio.sleep(7)
        await ctx.send("Ahhh don't care fucking retard.")

def setup(bot):
    bot.add_cog(Nigga(bot))