import discord
from discord.ext import commands
import json
with open("./data/infor.json", mode="r", encoding="utf-8") as file:
    infor=json.load(file)

from core.classes import cog_extension
from core import localization as loc

def language(id):
  with open("./data/guildinfo.json",mode="r",encoding="utf-8") as file:
    gdif=json.load(file)

  with open("./data/localization_pack.json",mode="r",encoding="utf-8") as data:
    lanpak=json.load(data)

  for x in gdif:
    if x == str(id):
      lan=gdif[x]["lan"]
      return lanpak[lan]
  return lanpak["zhtw"]

class meme(cog_extension):
    @commands.command()
    async def rick_roll(self, ctx):
      lan=language(ctx.guild.id)
      await ctx.send(lan["meme"]["1"])
      await ctx.send(infor["rick_roll"])
    #一個rick roll別人的指令

    @commands.command()
    async def drDisrespect(self, ctx):
        await ctx.send(infor["drDis"])
    #一個會出現Dr.disrespect的指令
    @commands.command()
    async def winnie(self,ctx):
      await ctx.send(infor["winnie"])
    @commands.command()
    async def knock_knock(self,ctx):
      await ctx.send(infor["son"])

def setup(bot):
    bot.add_cog(meme(bot))