import discord
import random
import asyncio
from discord.ext import commands

from core.classes import cog_extension

def jm(plyr,ai,ero):
  if ero=="yep":
    return "lol"
  if plyr=="r":
    if ai=="r":
      return "tie"
    if ai=="p":
      return "lose"
    if ai=="s":
      return "win"
  if plyr=="p":
    if ai=="p":
      return "tie"
    if ai=="s":
      return "lose"
    if ai=="r":
      return "win"
  if plyr=="s":
    if ai=="s":
      return "tie"
    if ai=="r":
      return "lose"
    if ai=="p":
      return "win"
#和猜拳相關的函式

class react(cog_extension):
    @commands.command()
    async def hello(self,ctx):
        await ctx.send("what's up sucker")
    #一個打招呼的指令

    @commands.command()
    async def rps(self,ctx,ms):
      ero="nope"
      if ms!="r" and ms!="p" and ms!="s":
        await ctx.send("你是連個拳都可以出錯是吧?")
        ero="yep"
      ai=random.choice(["r","p","s"])
      rst=jm(ms,ai,ero)
      if ero!="yep":
        await ctx.send("你出了"+ms+",電腦出了"+ai)
      await asyncio.sleep(1)
      if rst=="lose":
        await ctx.send("你輸了你這個魯蛇")
      if rst=="win":
        await ctx.send("你神奇的贏了")
      if rst=="tie":
        await ctx.send("你和他打成了平手")
    #一個猜拳的指令  


      

def setup(bot):
    bot.add_cog(react(bot))