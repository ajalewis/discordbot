from discord.ext import commands
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%d-%m-%Y %H:%M:%S')

class Ping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(description='The bot will reply with "Pong"',
               brief='Replies with "Pong"')
  async def ping(self, ctx):
    await ctx.send("Pong", delete_after=3)
    await ctx.message.delete()
    logging.info(f'{ctx.author} sent the !ping command')
    
async def setup(bot):
  await bot.add_cog(Ping(bot))