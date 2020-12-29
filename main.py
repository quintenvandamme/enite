import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Welcome Hexa')

@client.event  
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startwith('/version'):
    await message.channel.send('V 0.1.0')

client.run(os.getenv('TOKEN'))