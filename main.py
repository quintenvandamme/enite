import discord
import sys
import random
import time
import datetime
import os
from keep_alive import keep_alive
from discord.ext import commands
sys.path.append('/mnt/disk1/bot/')
from TOKEN_ENITE import token

# bot info
VERSION = "0.1.9"
SOURCE = "https://github.com/hexa-one/enite"

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

activity = discord.Game(name="Meow")

@client.event  
async def on_message(message):

  # server id
  guild_id = client.get_guild(753325735137116362)

  # mods
  mod_users = ["hexa#9096","Lars#8503","furkmeenistan#3286"]
  
  # commands
  if message.author == client.user:
    return

  if message.content.startswith('/version'):
    await message.channel.send(VERSION)

  if message.content.startswith('/github'):
    await message.channel.send(SOURCE)

  if message.content.startswith('/meow'):
    MEOW = "meow :cat2: :cat2:"
    await message.channel.send(MEOW)

  if message.content.startswith('/date'):
    today = datetime.date.today()
    DATE = today.strftime("20%y/%m/%d")
    await message.channel.send(DATE)

  ## latency (beta)
  if message.content.startswith('/latency'):
    time_1 = time.perf_counter()
    time_2 = time.perf_counter()
    ping = round((time_2-time_1)*1000)
    await message.channel.send(f"ping = {ping}")


## help command (embed) (beta)
  if message.content.startswith('/help'):
    embedVar = discord.Embed(title="Stats", description="", color="#3451E6")
    embedVar.add_field(name="Latency:", value=("/latency"), inline=True)
    embedVar.add_field(name="Bot Version:", value=("/version"), inline=False)
    embedVar.add_field(name="Test Mod:", value=("/testmod"), inline=False)
    embedVar.add_field(name="Date:", value=("/date"), inline=False)
    await message.channel.send(embed=embedVar)


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
  if message.content.startswith('!'):
    await channel.send(f"""```User:{message.author} tried {message.content} in #{message.channel}```""")
  if message.content.startswith('?'):
    await channel.send(f"""```User:{message.author} tried {message.content} in #{message.channel}```""")

# welcome users
@client.event
async def on_member_join(member):
  guild = client.get_guild(753325735137116362)
  channel = guild.get_channel(753325735795490929)
  await channel.send(f'Welcome! {member.mention}')

keep_alive() # for backup only

client.run(token)

