import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, BadArgument
import requests, json 
from datetime import timedelta, datetime
from module import *

GLOBAL = 0x03d692

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.has_permissions(kick_members=True)
    @commands.command()
    @isbanned()
    async def kick(self, ctx, user: discord.Member, *, reason="No reason provided"):
        print("kick")
        await user.kick(reason=reason)
        kick = discord.Embed(title=f"{user.name} has been kicked!", description=f"Reason: {reason}\nBy: {ctx.author.mention}", color=GLOBAL)
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)


    @commands.has_permissions(ban_members=True)
    @commands.command()
    @isbanned()
    async def ban(self, ctx, user: discord.Member, *, reason="No reason provided"):
        print("Ban")
        await user.ban(reason=reason)
        ban = discord.Embed(title=f"{user.name} has been banned!", description=f"Reason: {reason}\nBy: {ctx.author.mention}", color=GLOBAL)
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

    @commands.command(name='slowmode',  aliases=['Slowmode', 'slow', 'slowmo','Slow', 'Slowmo'])
    @has_permissions(manage_messages=True)
    @isbanned()
    async def slowmode(self, ctx, seconds: int):
        print("Slow")
        try:
            await ctx.channel.edit(slowmode_delay=seconds)
            embed = discord.Embed(title="Slowmode", description=f"Set the slowmode delay in this channel to {seconds} seconds!", color=discord.Color.blue())
        except:
            embed = discord.Embed(title="Slowmode", description="Couldn't set slowmode!", color=discord.Color.red())
        await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(mod(bot))