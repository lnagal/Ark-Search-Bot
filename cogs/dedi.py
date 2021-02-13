import discord, json, urllib.parse, urllib.request, json, requests, webbrowser, asyncio, numbers, random, time, math, os
from discord.ext import commands
from urllib.parse import urlencode
from urllib.request import urlopen
from discord import Activity, ActivityType
from module import *

GLOBAL = 0x03d692

class Dedi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dedi")
    @isbanned()
    async def dedi(self, ctx, *, name):
        print("Dedi Fetching Servers")
        response = requests.get("http://arkdedicated.com/xbox/cache/unofficialserverlist.json")
        data = response.json()
        keys_we_care_about = ["Name", "IP", "Port", "NumPlayers", "MapName"]
        embed = discord.Embed(title=' ', description=' ', color=0x2FD81B)
        for item in data:
            if name.lower() in item["Name"].lower():
                print("Found")
                embed.set_author(name=f'Results For {name}', icon_url='https://logodix.com/logo/20228.png')
                embed.set_footer(text='Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD')
                embed.add_field(name=f'{item["Name"]}', value=f'''
**IP: **`{item["IP"]}`
**Port: **`{item["Port"]}`
**Players: **`{item["NumPlayers"]}`
**Map: **`{item["MapName"]}`
''', inline=False)

        await ctx.send(embed=embed)

    @commands.command(name="dedipop")
    async def dedipop(self, ctx, *, name):
        print("DediPop Fetching Servers")
        xdedifile = ("dedi player")
        xmaxfile = ("xmax")
        response = requests.get("http://arkdedicated.com/xbox/cache/unofficialserverlist.json")
        data = response.json()
        keys_we_care_about = ["Name", "NumPlayers", "MaxPlayers"]
        for item in data:
            if name.lower() in item["Name"].lower():
                print("Found")
                newline = "\n"
                with open(xdedifile, 'a') as out:
                    out.write(f'{item["NumPlayers"]}'+newline)
                with open(xmaxfile, 'a') as out:
                    out.write(f'{item["MaxPlayers"]}'+newline)
            embed = discord.Embed(color=0x2FD81B)
            embed.set_author(name=f'Results For {name}', icon_url='https://logodix.com/logo/20228.png')
            embed.set_footer(text='Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD')

        with open(xdedifile,'r') as numbers_file:
            total = sum(int(line) for line in numbers_file if line.strip())
            with open(xmaxfile,'r') as numbers_file:
                dedimax = sum(int(line) for line in numbers_file if line.strip())
        print(total)
        print(dedimax)

        embed.add_field(name='''Players Found''', value=f"**Players: **`{total}/{dedimax}`", inline=True)
        await ctx.send(embed=embed)
        os.remove(xdedifile)
        os.remove(xmaxfile)
        time.sleep(10)


def setup(bot):
    bot.add_cog(Dedi(bot))