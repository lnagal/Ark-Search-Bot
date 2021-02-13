import discord, aiohttp, io, json, sys
from discord.ext import commands

def isbanned():
    async def predicate(ctx):
        with open("blacklist.json") as f:
            data = json.load(f)
        if ctx.author.id in data['BannedUsers']: 
            await ctx.send(f"{ctx.author.mention} Your banned from using this bot join our server make a ticket to be unbanned")
            f.close()
            return False
        f.close()
        return True
    return commands.check(predicate)

def isclay():
    async def predicate(ctx):
        if ctx.author.id == 808074820570710029: 
            return True
        else:
            return False
        return True
    return commands.check(predicate)