import discord
from discord.ext import commands
from module import *

GLOBAL = 0x03d692

class Xhelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['xh'])
    @isbanned()
    async def xhelp(self, ctx, commands=None):
        e1 = discord.Embed(title='Xbox Help', color=GLOBAL)
        e1_desc = f"**<----------Lookup Commands__----------**\n\n__Unofficial Xbox__\n***.dedi (Usage)***\n\n__Small Tribes Xbox__\n***.st (Usage)***\n\n__Official Xbox__\n***.ark (Usage)***\n\n**<----------Pop Commands__----------**\n\n__Unofficial Xbox__\n***.dedipop (Usage)***"
        e1.set_footer(text=f"Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD")
        e1.description = e1_desc

        await ctx.send(embed=e1)

def setup(bot):
    bot.add_cog(Xhelp(bot))