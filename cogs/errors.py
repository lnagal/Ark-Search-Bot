import discord, json
from discord.ext import commands
from module import *

GLOBAL = 0x03d692

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @isbanned()
    async def error(self, ctx, commands=None):
        print("Error")
        e1 = discord.Embed(color=GLOBAL)
        e1_desc = f"**<----------__Main Errors__---------->**\n\n__Empty Embed__\n***Means the server name doesn't exist***\n\n__Nothing when using .dedi__\n***Means you need to be more specific(Aka embed is to long)***"
        e1.set_footer(text=f"Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD")
        e1.description = e1_desc

        await ctx.send(embed=e1)

def setup(bot):
    bot.add_cog(Error(bot))