import discord, aiohttp, io, json, sys
from discord.ext import commands
from module import *


GLOBAL = 0x03d692

def isclay():
    async def predicate(ctx):
        if ctx.author.id == 808074820570710029: 
            return True
        else:
            return False
        return True
    return commands.check(predicate)

class Blacklist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @isclay()
    async def banuser(self, ctx, member: discord.Member):
        try:
            with open("blacklist.json") as f:
                ye = f.read()
            e = json.loads(ye)
            if member.id in e["BannedUsers"]:
                await ctx.send("Banning User")
            else:
                e["BannedUsers"].append(member.id)
                a_file = open("blacklist.json", "w")
                json.dump(e, a_file)
                a_file.close()
                f.close()
                await ctx.send("Success")
        except Exception as e:
            print(sys.exc_info()[-1].tb_lineno, e)

    @commands.command()
    @isclay()
    async def unbanuser(self, ctx, member: discord.Member):
        try:
            with open("blacklist.json") as f:
                ye = f.read()
            e = json.loads(ye)
            if member.id in e["BannedUsers"]:
                e["BannedUsers"].remove(member.id)
                a_file = open("blacklist.json", "w")
                json.dump(e, a_file)
                a_file.close()
                f.close()
                await ctx.send("User Unbanned")
            else:
                await ctx.send("User Not Banned")
        except Exception as e:
            print(sys.exc_info()[-1].tb_lineno, e)

def setup(bot):
    bot.add_cog(Blacklist(bot))