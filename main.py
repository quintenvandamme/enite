# import libs
import discord
import os
from keep_alive import keep_alive

# version
VERSION = "0.1.2"
GITHUB = "https://github.com/HexaOneOfficial/enite"

client = discord.Client()

@client.event
async def on_ready():
  print('Welcome Hexa')

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