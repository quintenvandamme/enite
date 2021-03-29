# import libs
import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
import datetime

# version
VERSION = "0.1.4"
GITHUB = "https://github.com/HexaOneOfficial/enite"
BUMP = "!d bump"


client = discord.Client()

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

keep_alive()

client.run(os.getenv('TOKEN')) 