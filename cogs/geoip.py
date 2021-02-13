import discord, aiohttp, io, requests, urllib, json
from discord.ext import commands
from module import *

GLOBAL = 0x03d692

class Geoip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @isbanned()
    async def geoip(self, ctx, message):
        ip = message
        lookup = ("http://ip-api.com/json/" + ip + "?fields=status,message,country,countryCode,region,regionName,city,zip,isp,as,query")
        with urllib.request.urlopen(lookup) as url:
            data = json.loads(url.read().decode())
        sts = ip
        if sts == "?":
            embed = discord.Embed(title="Error looking up " + ip, color=0xFF0008)
            embed.add_field(name="\nDouble check you've written the ip properly\n\nError:", value=data["message"])
            await ctx.send(embed=embed)
        else:
            country = data["country"]
            region = data["regionName"]
            city = data["city"]
            zip = data["zip"] + " (Prob not Correct)"
            isp = data["isp"]
            ipname = data["as"]
            status = data["status"]

            embed = discord.Embed(title="Geo Ip for " + ip,color=GLOBAL)
            embed.add_field(name="County:", value=country, inline=False)
            embed.add_field(name="Region:", value=region, inline=False)
            embed.add_field(name="City:", value=city, inline=False)
            embed.add_field(name="Zip:", value=zip, inline=False)
            embed.add_field(name="IpName:", value=ipname, inline=False)
            embed.add_field(name="Status:", value=status, inline=False)
            embed.set_footer(text='Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD')

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Geoip(bot))