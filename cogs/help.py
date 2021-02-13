import discord, json
from discord.ext import commands
from module import *

GLOBAL = 0x03d692


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['h'])
    @isbanned()
    async def help(self, ctx, commands=None):
        print("Help")
        e1 = discord.Embed(title='Help [Main Commands]', color=GLOBAL)
        e1_desc = f"**<----------__Main Commands__---------->**\n\n__Invite Me__\n***.invite***\n\n__Hydro Bot Status__\n***.status***\n\n__Set Prefix__\n***.setprefix (Usage)***\n\n__Show Bot Errors__\n***.error***\n\n__Xbox Ark Lookup__\n***.xhelp***\n\n__Play Station Ark Lookup__\n***.pshelp***\n\n**<----------__Moderation Commands__---------->**\n\n__Ban Members__\n***.ban (members) (reason)***\n\n__Kick Members__\n***.kick (Members) (Reason)***\n\n__Slowmode__\n***.slowmode (Usage)***\n\n__Purge Message__\n***.purge (Usage)***\n\n__Mute Members__\n***.mute (members) (reason)***\n\n__unmute Members__\n***.unmute (Members)***\n\n**<----------__Misc Commands__---------->**\n\n__Port Scanner__\n***.pscan (Usage)***\n\n__Who is__\n***.whois (Usage)***\n\n__Role Info__\n***.roleinfo (Usage)***\n\n__IP Lookup__\n***.geoip (Usage)***\n\n__Avatar__\n***.av (Usage)***\n\n__Deleted Message Sniper__\n***.snipe***\n\n__Shows Server Info__\n***.serverinfo***\n\n__Type An Embed Message__\n***.embed (Usage)***"
        e1.set_footer(text=f"Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD")
        e1.description = e1_desc

        await ctx.send(embed=e1)

def setup(bot):
    bot.add_cog(Help(bot))