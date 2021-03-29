# import libs
import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands
import datetime

# version
VERSION = "0.1.5"
GITHUB = "https://github.com/HexaOneOfficial/enite"

# intents
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=activity)
  print('Welcome Hexa')
activity = discord.Game(name="Being a cat")
  

@client.event  
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/version'):
    await message.channel.send(VERSION)

  if message.content.startswith('/github'):
    await message.channel.send(GITHUB)

@client.event
async def on_member_join(member):
  guild = client.get_guild(753325735137116362)
  channel = guild.get_channel(753325735795490929)
  await channel.send(f'Welcome! {member.mention}')

keep_alive()

client.run(os.getenv('TOKEN')) 