import discord, aiohttp, io, random
from discord.ext import commands
from module import *

GLOBAL = 0x03d692

class Roleinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ri', 'role'])
    @isbanned()
    async def roleinfo(self, ctx, *, role: discord.Role): # b'\xfc'
        print("Role Info")
        guild = ctx.guild
        since_created = (ctx.message.created_at - role.created_at).days
        role_created = role.created_at.strftime("%d %b %Y %H:%M")
        created_on = "{} ({} days ago)".format(role_created, since_created)
        users = len([x for x in guild.members if role in x.roles])
        if str(role.colour) == "#000000":
            colour = "default"
            color = ("#%06x" % random.randint(0, 0xFFFFFF))
            color = int(colour[1:], 16)
        else:
            colour = str(role.colour).upper()
            color = role.colour
        em = discord.Embed(colour=color)
        em.set_author(name=f"Name: {role.name}"
        f"\nRole ID: {role.id}")
        em.add_field(name="Users", value=users)
        em.add_field(name="Mentionable", value=role.mentionable)
        em.add_field(name="Hoist", value=role.hoist)
        em.add_field(name="Position", value=role.position)
        em.add_field(name="Managed", value=role.managed)
        em.add_field(name="Colour", value=colour)
        em.add_field(name='Creation Date', value=created_on)
        em.set_footer(text='Developer: Clayless | Hydro Discord: https://discord.gg/yuyg4QzPvD')
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Roleinfo(bot))