# import libs
import discord
import os

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

client.run(os.getenv('TOKEN')) 