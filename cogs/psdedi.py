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

    @commands.command(name="psdedi")
    @isbanned()
    async def psdedi(self, ctx, *, name):
        print("PS4 Fetching Servers")
        response = requests.get("http://arkdedicated.com/ps4/cache/unofficialserverlist.json")
        data = response.json()
        keys_we_care_about = ["Name", "IP", "Port", "NumPlayers", "MapName"]
        embed = discord.Embed(title=' ', description=' ', color=0x091BA1)
        for item in data:
            if name.lower() in item["Name"].lower():
                print("Found")
                embed.set_author(name=f'Results For {name}', icon_url='https://i.ibb.co/nD96Wnj/pngwing-com.png')
                embed.set_footer(text='Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD')
                embed.add_field(name=f'{item["Name"]}', value=f'''
**IP: **`{item["IP"]}`
**Port: **`{item["Port"]}`
**Players: **`{item["NumPlayers"]}`
**Map: **`{item["MapName"]}`
''', inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="psdedipop")
    async def psdedipop(self, ctx, *, name):
        print("PS4Pop Fetching Servers")
        psdedifile = ("psdedi player")
        psmaxfile = ("psmax")
        response = requests.get("http://arkdedicated.com/ps4/cache/unofficialserverlist.json")
        data = response.json()
        keys_we_care_about = ["Name", "NumPlayers", "MaxPlayers"]
        for item in data:
            if name.lower() in item["Name"].lower():
                print("Found")
                newline = "\n"
                with open(psdedifile, 'a') as out:
                    out.write(f'{item["NumPlayers"]}'+newline)
                with open(psmaxfile, 'a') as out:
                    out.write(f'{item["MaxPlayers"]}'+newline)
            embed = discord.Embed(color=0x091BA1)
            embed.set_author(name=f'Results For {name}', icon_url='https://i.ibb.co/nD96Wnj/pngwing-com.png')
            embed.set_footer(text='Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD')

        with open(psdedifile,'r') as numbers_file:
            total = sum(int(line) for line in numbers_file if line.strip())
            with open(psmaxfile,'r') as numbers_file:
                dedimax = sum(int(line) for line in numbers_file if line.strip())
        print(total)
        print(dedimax)

        embed.add_field(name='''Players Found''', value=f"**Players: **`{total}/{dedimax}`", inline=True)
        await ctx.send(embed=embed)
        os.remove(psdedifile)
        os.remove(psmaxfile)
        time.sleep(10)

def setup(bot):
    bot.add_cog(Dedi(bot))