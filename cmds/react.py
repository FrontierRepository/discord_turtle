import discord
import random
import asyncio
import json
from discord.ext import commands

from core.classes import cog_extension

with open("meme.json",mode="r",encoding="utf-8") as file:
  meda=json.load(file)

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
    @commands.command()
    async def guess_meme(self,ctx):
      self.lim=round(random.uniform(1,29))
      self.count=0
      for x in meda:
        if self.count<self.lim:
          self.ans=x
        self.count=self.count+1
      #隨機獲得圖片
      await ctx.send("這是哪個迷因")
      await ctx.send(meda[self.ans])

      def check(m):
        return m.content==str(self.ans) and m.channel==ctx.channel and m.author==ctx.author
      
      try:
        self.msg=await self.bot.wait_for(event="message", check=check, timeout=20)
      except asyncio.TimeoutError:
        await ctx.send("超時了你這SB,答案是"+self.ans)
      else:
        await ctx.send("正確答案")
      #玩猜迷因的指令

def setup(bot):
    bot.add_cog(react(bot))