import discord, json, urllib.parse, urllib.request, json, requests, webbrowser, asyncio, numbers, random, time, math, os
from discord.ext import commands
from urllib.parse import urlencode
from urllib.request import urlopen
from discord import Activity, ActivityType
from module import *

GLOBAL = 0x03d692

class Official(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_name(self, text, search):
        numbers = '0123456789'
        servern = ''.join([s for s in text if s in list(numbers)])
        server = ''.join([s for s in text if search == servern])
        if search == servern: return server

    @commands.command(name="ark")
    @isbanned()
    async def ark(self, ctx, *, name):
        with urlopen("http://arkdedicated.com/xbox/cache/officialserverlist.json") as response:
            source = response.read()
            data = json.loads(source)
            keys_we_care_about = ["Name", "IP", "Port", "NumPlayers", "DayTime", "MapName"]
            embed = discord.Embed(color = 0x2FD81B)
            for item in data:
                if name.lower() in item["Name"].lower():
                    embed.set_author(name=f'Results For {name}', icon_url='https://logodix.com/logo/20228.png')
                    embed.set_footer(text='Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD')
                    embed.add_field(name=f'{item["Name"]}', value=f'''
**Players: **{item["NumPlayers"]}
**IP: **{item["IP"]}
**Port: **{item["Port"]}
**Map: **{item["MapName"]}
''', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Official(bot))