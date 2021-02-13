import discord, json, urllib.parse, urllib.request, requests, webbrowser, asyncio, numbers, random, time, math, os, platform, datetime, numpy, logging
from discord.ext import commands
from urllib.parse import urlencode
from urllib.request import urlopen
from discord import Activity, ActivityType
from module import *

def get_prefix(bot, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes.get(str(message.guild.id), ".")

GLOBAL = 0x03d692

cfg = open("config.json", "r")
tmpconfig = cfg.read()
cfg.close()
config = json.loads(tmpconfig)
token = config["token"]
start_time = datetime.datetime.utcnow()
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
intents.reactions = True
intents.webhooks = True
bot = commands.Bot(command_prefix=get_prefix, intents=intents, case_insensitive=False)
bot.remove_command("help")

if __name__ == "__main__":
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

def get_name(text, search):
    numbers = '0123456789'

    servern = ''.join([s for s in text if s in list(numbers)])
    server = ''.join([s for s in text if search == servern])

    if search == servern: return server

#__________________________________________________________________________________________________


@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "."
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@bot.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@bot.command()
@commands.has_permissions(administrator=True)
@isbanned()
async def setprefix(ctx, prefix):
    print("Set prefix")
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f"Prefix changed to: {prefix}")

@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
@isbanned()
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    mute = discord.Embed(title=f"{member.name} has been muted!", description=f"Reason: {reason}\nBy: {ctx.author.mention}", color=GLOBAL)
    await ctx.send(embed=mute)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(embed=mute)

@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
@isbanned()
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" You have been unmutedd from: {ctx.guild.name}")
   unmute = discord.Embed(title=f"{member.name} has been unmuted!", description=f"By: {ctx.author.mention}", color=GLOBAL)
   await ctx.send(embed=unmute)

snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@bot.command(name='snipe')
@isbanned()
async def snipe(ctx):
    print("Snipe")
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=GLOBAL)
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]} - If Embed is empty Means The Msg Deleted was Image or Embed")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}!")

#__________________________________________________________________________________________________


@bot.command(name="st")
@isbanned()
async def st(ctx, *, name):
    
    with urlopen("http://arkdedicated.com/xbox/cache/officialserverlist.json") as response:
        source = response.read()
        data = json.loads(source)
        keys_we_care_about = ["Name", "IP", "Port", "NumPlayers", "DayTime"]
        embed = discord.Embed(title=' ', description=' ', color=0x2FD81B)
        for item in data:
            the_server = get_name(item["Name"], str(name))
            if item["Name"] == the_server and 'SmallTribes' in item["Name"] and 'XboxOfficial' in the_server:
                embed.set_author(name=f'Results For {name}', icon_url='https://logodix.com/logo/20228.png')
                embed.set_footer(text='Developer: n a g a | Kanami Discord: https://discord.gg/dkfjan')
                embed.add_field(name=f'{item["Name"]}', value=f'''
**IP: **`{item["IP"]}`
**Port: **`{item["Port"]}`
**Players: **`{item["NumPlayers"]}`
**Map: **`{item["MapName"]}`
''', inline=False)

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def status(ctx):
        uptime = datetime.datetime.utcnow() - start_time
        uptime = str(uptime).split('.')[0]
        e1 = discord.Embed(title='Kanami Ark Lookup Status', color=0x03d692)
        e1_desc = f"__Kanami Uptime__\n***{uptime}***\n\n__Discords Using Kanami__\n***{len(bot.guilds)}***\n\n__All Kanami Users__\n***{(len(set(bot.get_all_members())))}***\n\n__Kanami's Ping__\n***{round(bot.latency * 1000)}ms***"
        e1.set_footer(text=f"Developer: n a g a | Kanami Discord: https://discord.gg/adfadfgas")
        e1.description = e1_desc

        await ctx.send(embed=e1)

"""
invites = {}
last = ""

async def fetch():
    global last
    global invites
    await bot.wait_until_ready()
    gld = bot.get_guild(int(801463306979508224))
    logs = bot.get_channel(int(801468584270233630))
    while True:
        invs = await gld.invites()
        tmp = []
        for i in invs:
            for s in invites:
                if s[0] == i.code:
                    if int(i.uses) > s[1]:
                        usr = gld.get_member(int(last))
                        eme = discord.Embed(description="Just joined the server", color=0x03d692, title=" ")
                        eme.set_author(name=usr.name + "#" + usr.discriminator, icon_url=usr.avatar_url)
                        eme.set_footer(text="ID: " + str(usr.id))
                        eme.timestamp = usr.joined_at
                        eme.add_field(name="Used invite",
                                      value="Inviter: " + i.inviter.mention + " (`" + i.inviter.name + "#" + i.inviter.discriminator + "`)\nCode: `" + i.code + "`\nUses: `" + str(
                                          i.uses) + "`", inline=False)
                        await logs.send(embed=eme)
            tmp.append(tuple((i.code, i.uses)))
        invites = tmp
        await asyncio.sleep(4)
"""

async def status():
    while True:
        await bot.wait_until_ready()
        await bot.change_presence(activity=discord.Game(name="Kanami Ark Lookup"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name=f"with {(len(set(bot.get_all_members())))} Users | .help"))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(name=f"on {len(bot.guilds)} servers | .help"))
        await asyncio.sleep(15)
@bot.event
async def on_ready():
    print(f'{(bot.user)} has Awoken!')
bot.loop.create_task(status())

@bot.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        await ctx.send(f'[ERROR]: {error_str}', delete_after=3)

bot.run(token)