import discord
from discord.ext import commands
import json
import requests

with open("./data/infor.json", mode="r", encoding="utf-8") as file:
    infor=json.load(file)

from core.classes import cog_extension
from core import localization as loc

def language(id):
  response=requests.get("https://getpantry.cloud/apiv1/pantry/01865685-19e7-4f85-9aa8-d8da22683475/basket/cute_turtle_guildinfo")
  gdif=response.json()

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