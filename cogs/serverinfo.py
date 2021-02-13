import discord, aiohttp, io, asyncio, datetime
from discord.ext import commands
from module import *

GLOBAL = 0x03d692

class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["guildinfo"])
    @isbanned()
    async def serverinfo(self, ctx):
        print("Server Info")
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(title=f"{ctx.guild.name}",
                            description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories", color=GLOBAL)
        embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
        embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        embed.set_footer(text='Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Serverinfo(bot))