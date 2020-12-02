#---------------------------------------------------------------------------------------------------- 
# imports
import re, sys, json, asyncio, discord
from sorter import user_request
from discord.voice_client import *
from discord.ext import commands
from discord.utils import get

#----------------------------------------------------------------------------------------------------
# kick off event

client_id = 'apikey'
bot = commands.Bot(command_prefix="!")

#----------------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
  print('\n')
  print('The casino is Online')
  print('\n')

#----------------------------------------------------------------------------------------------------

@bot.command(pass_context=True)
async def slots(ctx, wager):
  user_id = ctx.message.author.id
  channel = ctx.message.channel.id
  response = user_request(str(user_id), ['slots', int(wager)])
  print(response)
  if response == 'not enough minerals':
    await ctx.message.channel.send('not enough minerals')
  else:
    with open('games/images/slot.gif', 'rb') as fp:
      await ctx.message.channel.send(file=discord.File(fp, 'games/images/slot.gif'))
      if response > 0:
          await ctx.message.channel.send('Player won' + ' $' + str(response))

@bot.command(pass_context=True)
async def wallet(ctx):
  user_id = str(ctx.message.author.id)
  channel = ctx.message.channel.id
  await ctx.message.channel.send(user_request(user_id, ['wallet']))

@bot.command(pass_context=True)
async def league(ctx, bet_type, wager):
  user_id = str(ctx.message.author.id)
  channel = ctx.message.channel.id
  if user_request(str(user_id), ['league', bet_type, wager]) == 'not enough minerals':
    print('not enough minerals')
  else:
    user_request(user_id, ['league', bet_type, wager])
    await ctx.message.channel.send('bet placed')

@bot.command(pass_context=True)
async def troll(ctx):
  user_id = str(ctx.message.author.id)
  channel = ctx.message.channel.id
  response = user_request(user_id, ['troll'])
  await ctx.message.channel.send(response)

@bot.command(pass_context=True)
async def add_stream(ctx, url):
  user_id = str(ctx.message.author.id)
  channel = ctx.message.channel.id
  response = user_request(user_id, ['add_stream', url])
  await ctx.message.channel.send(response)

@bot.command(pass_context=True)
async def live(ctx):
  user_id = str(ctx.message.author.id)
  channel = ctx.message.channel.id
  response = user_request(user_id, ['live'])
  await ctx.message.channel.send('@everyone ' + response + ' is live!')

#----------------------------------------------------------------------------------------------------
# start the bot
bot.run(client_id)
#----------------------------------------------------------------------------------------------------