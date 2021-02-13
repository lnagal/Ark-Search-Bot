import discord
from discord.ext import commands
from module import *

GLOBAL = 0x03d692

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="invite")
    @isbanned()
    async def invite(self, ctx):
        print("invite")
        embed = discord.Embed(title='Hydro Ark Lookup Bot', description=('__https://discord.gg/DYenHGUpTH__'), color = 0x03d692)
        embed.set_author(name='Click Me', url='https://discord.com/oauth2/authorize?client_id=804133105244831806&permissions=8&scope=bot')
        embed.set_footer(text='Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Invite(bot))