import discord, requests
from typing import Optional
from discord.ext import commands
from module import *

GLOBAL = 0x03d692

class pscan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @isbanned()
    async def pscan(self, ctx, arg1):
        print("Pscan")
        await ctx.message.delete()
        scanyuh = requests.get("https://api.hackertarget.com/nmap/?q=%s" % arg1)
        result = scanyuh.text.strip(" ( https://nmap.org/ )")
        embed = discord.Embed(title='''**Hydro Port Scanner**''', description=f"**{result}**", color=GLOBAL)
        embed.set_footer(text='Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD | Pscan Made by Root')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(pscan(bot))