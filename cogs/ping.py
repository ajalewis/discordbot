from discord.ext import commands
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%d-%m-%Y %H:%M:%S')

class Ping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def ping(self, ctx):
    await ctx.send("Pong")
    logging.info(f'{ctx.author} sent the !ping command')
    
async def setup(bot):
  await bot.add_cog(Ping(bot))