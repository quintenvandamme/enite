import discord
import os

VERSION = "0.1.1"

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

client.run(os.getenv('TOKEN'))