import time
import os
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
  intents = discord.Intents.default()
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
      
  @bot.command(description='Will randomize players up to 4 teams of 2 or 3 per team. Run !shuffle and then enter names separated by a space. Names can be @<USER> or normal strings.',
               brief='Shuffles players into teams up 4.')
  async def shuffle(ctx):
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
      response_not_enough = await ctx.send(
        f"{ctx.author.mention} You didn't enter enough players! Please try again ", delete_after=5
      )
      await ctx.message.delete()
    else:
      await ctx.send(embed=embed, delete_after=300)
      await ctx.message.delete()

  bot.run(token)


discord_bot()