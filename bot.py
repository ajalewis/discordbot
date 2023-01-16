import time
import os
import re
import discord
import asyncio
import random
from discord.ext import commands
from dotenv import load_dotenv
from commands.shuffle_teams import *

def discord_bot():
  load_dotenv()
  token = os.getenv('token_dev')
  activity = discord.Activity(type=discord.ActivityType.watching, name="Zealots Server")
  intents = discord.Intents.all()
  intents.message_content = True
  bot = commands.Bot(command_prefix='!', intents=intents, activity=activity)

  async def reply(ctx, message: str):

    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel and len(
        message.split()) >= 3

    question = await ctx.send(message)
    response = await bot.wait_for("message", check=check, timeout=35.0)
    await question.delete()
    await response.delete()

    return str(response.content)

  @bot.event
  async def on_ready():
    print(f'{bot.user} is up and running')
    
  @bot.event
  async def on_command_error(ctx, e):
    if ctx.author == bot.user :
      return
    await ctx.send(f"{ctx.author.mention} That is not a valid command. Please run !help to list them") 
          
  @bot.command(description='Will randomize players up to 4 teams of 2 or 3 per team. Run !shuffle and then enter names separated by a space. Names can be @<USER> or normal strings.',
               brief='Shuffles players into teams up 4.')
  async def shuffle(ctx):
    voice_channel = ctx.author.voice
    if voice_channel == None:
        await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to run this command!", delete_after=5)
        await ctx.message.delete()
        return
    try:
        players = await reply(ctx, "Please list at least 4 players")
        shuffled_players = players.split()
        random.shuffle(shuffled_players)
    except asyncio.TimeoutError:
      await ctx.send(f"{ctx.author.mention} You were too slow to answer!", delete_after=5)
      return
    else:
      z = team_one(shuffled_players)
      y = team_two(shuffled_players)

    embed = discord.Embed(title="------- **TEAMS** -------",
                          color=0xFFFFFF,
                          description="The shuffled teams are now:")
    embed.set_thumbnail(
      url=
      "https://cdn.discordapp.com/attachments/338614846125899777/1059762564059369502/the-punisher-wallpaper-preview.png"
    )
    embed.add_field(name="Team 1:", value=z, inline=True)
    embed.add_field(name="Team 2:", value=y, inline=True)
    embed.set_footer(text=f'The teams where generated by {ctx.author.name} 🎉')

    if None in (z, y):
      await ctx.send(
        f"{ctx.author.mention} You didn't enter enough players! Please try again ", delete_after=5
      )
      await ctx.message.delete()
    else:
      vc_connected = ctx.author.voice.channel
      vc = await vc_connected.connect()
      vc.play(discord.FFmpegPCMAudio(source="tick-wheel.mp3"))
      while vc.is_playing():
        with open('wheel.gif', 'rb') as f:
          gif = discord.File(f)
        await ctx.send(content='Spinning the wheel!  🤓', delete_after=0, file=gif)
        time.sleep(8)
        break
        time.sleep(1)
      await vc.disconnect()
      await ctx.send(embed=embed, delete_after=300)
      await ctx.message.delete()

  bot.run(token)

discord_bot()