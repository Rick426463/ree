import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import os

client = commands.Bot(command_prefix='??thebot678593083249473892')

@client.event
async def on_ready():
  print(f'[{client.user.name} is online]')

@client.event
async def on_message(message):
  channel = client.get_channel('552913888169951272')
  if message.attachments:
    for x in message.attachments:
      name = x['filename']
      url = x['url']

    embed = discord.Embed(title=f'{name}',colour=discord.Colour(random.randint(0x000000,0xFFFFFF)))
    embed.set_image(url=url)
    await client.send_message(channel, embed=embed)

client.run(os.getenv('NTQ5MTQ0ODg0MjIxNTc1MTY4.D2Fk9A.8e31CbVYQ1TKOrgeu3Z3-3GsI7o'),bot=False)
