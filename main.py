import discord
import os
import random
import time
from keep_alive import keep_alive
from discord.ext import commands
import datetime

# version
VERSION = "0.1.7"
SOURCE = "https://github.com/HexaOneOfficial/enite"

# commands_id
MEOW = "meow :cat2: :cat2:"

# intents
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=activity)
  print('Welcome Hexa')
  
  channel = client.get_channel(826049329755586592)
  await channel.send(f"""```Ready```""")

activity = discord.Game(name="Being a cat")

@client.event  
async def on_message(message):

  # server id
  guild_id = client.get_guild(753325735137116362)

  # mod users
  mod_users = ["hexa#8439","Lars#8503","Twg#9531"]
  
  # commands
  if message.author == client.user:
    return

  if message.content.startswith('/version'):
    await message.channel.send(VERSION)

  if message.content.startswith('/github'):
    await message.channel.send(SOURCE)

  if message.content.startswith('/meow'):
    await message.channel.send(MEOW)

  ## test only
  if message.content.startswith('/build-ionix'):
    guild = client.get_guild(753325735137116362)
    channel = guild.get_channel(826028712474574888)
    file = discord.File("assets/cat.png")
    await channel.send("hexa's pfp", file=file)

  if message.content.startswith('/build-album'):
    guild = client.get_guild(753325735137116362)
    channel = guild.get_channel(825694784567115776)
    await channel.send(f"""```Starlight2022-rc1``` `Download:` https://gitlab.com/HexaOneOfficial/starlight-2022/-/archive/master/starlight-2022-master.zip""")

  if message.content.startswith('/latency'):
    time_1 = time.perf_counter()
    time_2 = time.perf_counter()
    ping = round((time_2-time_1)*1000)
    await message.channel.send(f"ping = {ping}")

## old stats code
  #if message.content == "/stats":
    #await message.channel.send(f"""```Members: {guild_id.member_count}
#Version: {VERSION}
#Source: {SOURCE}```""")

  ## stats command (embed)
  if message.content.startswith('/stats'):
    embedVar = discord.Embed(title="Stats", description="", color=0x00ff00)
    embedVar.add_field(name="Members:", value=(guild_id.member_count), inline=True)
    embedVar.add_field(name="Version:", value=(VERSION), inline=False)
    time_1 = time.perf_counter()
    time_2 = time.perf_counter()
    ping = round((time_2-time_1))    
    embedVar.add_field(name="Latency:", value=(f"{((time_1-time_2)*1000)}ms"), inline=False)     
    embedVar.add_field(name="Source:", value=(SOURCE), inline=False)    
    await message.channel.send(embed=embedVar)


  # mod only commands
  ## test command
  if message.content.startswith('/testmod') and str(message.author) in mod_users:
    await message.channel.send(MEOW)
  else: # checks if a user uses a / command
    channel = client.get_channel(826049329755586592)
  if message.content.startswith('/'):
    await channel.send(f"""```User:{message.author} tried {message.content} in #{message.channel}```""")

# welcome users
@client.event
async def on_member_join(member):
  guild = client.get_guild(753325735137116362)
  channel = guild.get_channel(753325735795490929)
  await channel.send(f'Welcome! {member.mention}')

keep_alive()

client.run(os.getenv('TOKEN')) 