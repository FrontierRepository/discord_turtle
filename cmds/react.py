import discord
import random
import asyncio
import sys
import requests
import json
from discord.ext import commands

from core.classes import cog_extension

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

class react(cog_extension):
    @commands.command()
    async def hello(self,ctx):
        await ctx.send("what's up sucker")
    #一個打招呼的指令

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def delete(self,ctx,num):
      lan=language(ctx.guild.id)
      await ctx.channel.purge(limit=int(num)+1)
      await ctx.send(lan["react"]["1"]+num+lan["react"]["2"])
      await asyncio.sleep(2)
      await ctx.channel.purge(limit=1)
    @commands.command()
    async def path(self,ctx):
      print(sys.path)
    
    @commands.command()
    async def role_list(self,ctx):
      for role in ctx.guild.roles:
        await ctx.send(role.name) 

    @commands.command()
    async def test(self, ctx):
      pass
    
    @commands.command()
    async def update(self, ctx,*,msg):
      if ctx.author.id != 465866092875612189:
        await ctx.send("你沒有這個權限")
        return
      with open("./data/guildinfo.json", mode="r", encoding="utf") as file:
        data=json.load(file)
      for x in data:
        if data[x]["id"]!="None":
          channel=self.bot.get_channel(data[x]["id"])
          await channel.send(msg)



def setup(bot):
    bot.add_cog(react(bot))