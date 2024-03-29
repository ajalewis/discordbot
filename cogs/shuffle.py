from discord.ext import commands
import discord
import time
import random
import asyncio
import logging


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%d-%m-%Y %H:%M:%S')

class Shuffle(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
    
    def team_one(self, shuffled_players):
      if len(shuffled_players) <= 3:
          logging.error("No need to shuffle teams less than 3")
          return
      elif len(shuffled_players) == 4:
          one = shuffled_players[0:2]
          dash = "- "
          one_dash = [dash + x for x in one]
          team_one = '\n'.join(one_dash)
          logging.info("Teams have been sorted")
          print(f'{team_one}')
          return team_one
      else:
          one = shuffled_players[0:3]
          dash = "- "
          one_dash = [dash + x for x in one]
          team_one = '\n'.join(one_dash)
          logging.info("Teams have been sorted")
          logging.info(f'{team_one}')

      return team_one

    def team_two(self, shuffled_players):

        if len(shuffled_players) <= 3:
            logging.error("No need to shuffle teams less than 3")
            return
        elif len(shuffled_players) == 4:
            two = shuffled_players[2:5]
            dash = "- "
            two_dash = [dash + x for x in two]
            team_two = '\n'.join(two_dash)
            logging.info("Teams have been sorted!")
            print(f'{team_two}')
            return team_two
        else:
            two = shuffled_players[3:7]
            dash = "- "
            two_dash = [dash + x for x in two]
            team_two = '\n'.join(two_dash)
            logging.info("Teams have been sorted!")
            print(f'{team_two}')

        return team_two
     
    @commands.command(description='Will randomize players in teams of 2 or 3 per team. Run !shuffle and then enter names separated by a space. Names can be @<USER> or free text.',
               brief='Shuffles players into teams of 2.')
    async def shuffle(self, ctx):
      voice_channel = ctx.author.voice
      if voice_channel == None:
          await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to run the !shuffle command!", delete_after=5)
          await ctx.message.delete()
          return
      try:
          players = await self.reply(ctx, "Please list at least 4 players")
          shuffled_players = players.split()
          random.shuffle(shuffled_players)
      except asyncio.TimeoutError:
        await ctx.send(f"{ctx.author.mention} You were too slow to answer!", delete_after=5)
        return
      else:
        z = self.team_one(shuffled_players)
        y = self.team_two(shuffled_players)

      embed = discord.Embed(title="------- **TEAMS** -------",
                            color=0xFFFFFF,
                            description="The shuffled teams are now:")
      embed.set_thumbnail(
        url=
        "https://i.ibb.co/g9XG1k5/output-onlinepngtools.png"
      )
      embed.add_field(name="Team 1:", value=z, inline=True)
      embed.add_field(name="Team 2:", value=y, inline=True)
      embed.set_footer(text=f'The teams were generated by {ctx.author.name} 🎉')

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
        logging.info(f'{ctx.author} sent the !shuffle command')
        
    async def reply(self, ctx, message: str):
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and len(
          message.split()) >= 3

      question = await ctx.send(message)
      response = await self.bot.wait_for("message", check=check, timeout=35.0)
      await question.delete()
      await response.delete()

      return str(response.content)

async def setup(bot):
  await bot.add_cog(Shuffle(bot))