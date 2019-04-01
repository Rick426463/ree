import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import asyncio
import json
import string

client = commands.Bot(command_prefix = '?')
is_spamming = True

@client.event
async def on_message(message):
  with open('idk.json') as i:
    idk = json.load(i)

  if message.content.lower() == '?ping':
    await client.send_message(message.channel, 'Hey lol')

  if message.embeds:
    content = message.embeds[0]

    if content['title'] == '\u200c\u200cA wild pokémon has appeared!' or content['description'] == 'Guess the pokémon and type p!catch <pokémon> to catch it!':

      for x in idk:

        if not content['image']['url'] in idk[x]['url']:
          name = len(idk) + 1

          idk[name] = {}
          idk[name]['url'] = content['image']['url']
          idk[name]['proxy_url'] = content['image']['proxy_url']

          with open('idk.json', 'w') as i:
              json.dump(idk, i)


  if message.content.lower() == '?start spam':
    global is_spamming
    is_spamming = True
    while is_spamming:
      word = ''
      time = random.randint(1, 2)

      for x in range(1, 11):
          word += random.choice(list(string.ascii_letters))

      await client.send_typing(message.channel)
      await asyncio.sleep(time)
      await client.send_message(message.channel, word)

  if message.content.lower() == '?stop spam':
      is_spamming = False

  if message.content.lower() == '?request':
    await client.send_file(message.channel,'idk.json')

  await client.process_commands(message)

client.run('NTU2NDY2MjIwNjk0NjM0NDk2.XKIMKA.ayMMGLikrDo-6JURvbHqHduhps4', bot = False)
