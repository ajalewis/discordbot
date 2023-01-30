# Discord bot for Zealots.
# By alexanderashworthlewis@gmail.com

import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging
import os
import asyncio

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%d-%m-%Y %H:%M:%S')

load_dotenv()
token = os.getenv('token_dev')
activity = discord.Activity(type=discord.ActivityType.watching, name="Zealots Server")
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, activity=activity)

@bot.event
async def on_ready():
  logging.info(f'{bot.user} is up and running')

async def load_extensions():  
  for f in os.listdir("./cogs"):
    if f.endswith(".py"):
      await bot.load_extension("cogs." + f[:-3])

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

asyncio.run(main())