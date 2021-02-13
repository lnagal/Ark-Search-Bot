import discord
from discord.ext import commands
from module import *


GLOBAL = 0x03d692

class PS4help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['psh'])
    @isbanned()
    async def pshelp(self, ctx, commands=None):
        e1 = discord.Embed(title='PS4 Help', color=GLOBAL)
        e1_desc = f"**<----------__Lookup Commands__----------**\n\n__Unofficial PS4__\n***.psdedi (Usage)***\n\n__Small Tribes PS4__\n***No Api Yet***\n\n__Official PS4__\n***No Api Yet***\n\n**<----------Pop Commands__----------**\n\n__Unofficial PS4__\n***.psdedipop (Usage)***"
        e1.set_footer(text=f"Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD")
        e1.description = e1_desc

        await ctx.send(embed=e1)

def setup(bot):
    bot.add_cog(PS4help(bot))