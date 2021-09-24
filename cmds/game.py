
import discord
import random
import asyncio
import json
import os
import requests

from discord.ext import commands

from core.classes import cog_extension


for filename in os.listdir("./cmds"):
  if filename == "meme.json":
      with open("data."+str(filename) ,mode="r",encoding="utf-8") as file:
        meda=json.load(file)

sign={
  "r":"🌑",
  "p":"📄",
  "s":"✂"
}

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

class game(cog_extension):
  @commands.command()
  async def rps(self,ctx,ms):
    lan=language(ctx.guild.id)
    ero="nope"
    if ms!="r" and ms!="p" and ms!="s":
      await ctx.send(lan["game"]["1"])
      ero="yep"
    ai=random.choice(["r","p","s"])
    rst=jm(ms,ai,ero)
    if ero!="yep":
      await ctx.send(lan["game"]["2"]+sign[ms]+lan["game"]["3"]+sign[ai])
    await asyncio.sleep(1)
    if rst=="lose":
      await ctx.send(lan["game"]["4"])
    if rst=="win":
      await ctx.send(lan["game"]["5"])
    if rst=="tie":
      await ctx.send(lan["game"]["6"])
    #一個猜拳的指令  
  
  @commands.command()
  async def guess_meme(self,ctx):
    lan=language(ctx.guild.id)
    with open("./data/meme.json" ,mode="r",encoding="utf-8") as file:
      meda=json.load(file)

    self.maxium=0
    for x in meda:
      self.maxium=self.maxium+1
    self.lim=round(random.uniform(1,self.maxium))
    self.count=0
    for y in meda:
      if self.count<self.lim:
        self.ans=y
      self.count=self.count+1
    #隨機獲得圖片
    await ctx.send(lan["game"]["7"])
    await ctx.send(meda[self.ans])

    def check(m):
      return m.content==str(self.ans) and m.channel==ctx.channel and m.author==ctx.author
      
    try:
      self.msg=await self.bot.wait_for(event="message",check=check, timeout=25)
    except asyncio.TimeoutError:
      await ctx.send(lan["game"]["8"]+self.ans)
    else:
      await ctx.send(lan["game"]["9"])
    #玩猜迷因的指令
  
  @commands.command()
  async def war_ship(self,ctx):
    lan=language(ctx.guild.id)
    with open("./data/infor.json" ,mode="r",encoding="utf-8") as file:
      infor=json.load(file)

    user1=ctx.author
   
    await ctx.send("@here")     
    await ctx.send(lan["game"]["10"])     

    def check(m):
      return m.content=="+1" and m.author!=ctx.author and m.channel==ctx.channel
    try:
      msg=await self.bot.wait_for(event="message", check=check, timeout=30)
    except asyncio.TimeoutError:
      await ctx.send(lan["game"]["11"])
      return
    else:
      await ctx.send(lan["game"]["12"])
      await ctx.send(lan["game"]["13"]+":"+str(msg.author))
    user2=msg.author

    channel1=await ctx.guild.create_text_channel("player1")
    channel2=await ctx.guild.create_text_channel("player2")
    

    for member in ctx.guild.members:
      if member.id==846932821397995540:
        await channel1.set_permissions(member,view_channel=True)
        await channel2.set_permissions(member,view_channel=True)
        
      
      if member==user1:
        await channel1.set_permissions(member,view_channel=True)
      if member==user2:
        await channel2.set_permissions(member,view_channel=True)

    for role in ctx.guild.roles:
      if role.name=="@everyone":
        await channel1.set_permissions(role,view_channel=False)
        await channel2.set_permissions(role,view_channel=False)
    await channel1.send(lan["game"]["14"]+user1.mention)
    await channel2.send(lan["game"]["14"]+user2.mention)
    await channel1.send(infor["25"])
    await channel2.send(infor["25"])
    await channel1.send(lan["game"]["15"])
    await channel2.send(lan["game"]["16"])

    def check2(m):
      return m.channel==channel1
    
    try:
      p1msg=await self.bot.wait_for(event="message", check=check2, timeout=10)
    except asyncio.TimeoutError:
      await channel1.send(lan["game"]["17"])
      await channel2.send(lan["game"]["18"])
      await asyncio.sleep(5)
      await channel1.delete()
      await channel2.delete()
      return
    else:
      try:
        p1ship=int(p1msg.content)
      except:
        await channel1.send(lan["game"]["19"])
        await channel2.send(lan["game"]["18"])
        await asyncio.sleep(5)
        await channel1.delete()
        await channel2.delete()
        return
      else:
        if p1ship>25 or p1ship<1:
          await channel1.send(lan["game"]["19"])
          await channel2.send(lan["game"]["18"])
          await asyncio.sleep(5)
          await channel1.delete()
          await channel2.delete()
          return
    
    await channel2.send(lan["game"]["15"])
    await channel1.send(lan["game"]["16"])

    def check3(m):
      return m.channel==channel2
    try:
      p2msg=await self.bot.wait_for(event="message", check=check3, timeout=10)
    except asyncio.TimeoutError:
      await channel2.send(lan["game"]["17"])
      await channel1.send(lan["game"]['18'])
      await asyncio.sleep(5)
      await channel1.delete()
      await channel2.delete()
      return
    else:
      try:
        p2ship=int(p2msg.content)
      except:
        await channel1.send(lan["game"]["19"])
        await channel2.send(lan["game"]["18"])
        await asyncio.sleep(5)
        await channel1.delete()
        await channel2.delete()
        return
      else:
        if p2ship>25 or p2ship<1:
          await channel2.send(lan["game"]["19"])
          await channel1.send(lan["game"]["18"])
          await asyncio.sleep(5)
          await channel1.delete()
          await channel2.delete()
          return

    count=0
    winner="none"
    while count<10:
      await channel1.send(lan["game"]["20"])
      await channel2.send(lan["game"]["21"])

      try:
        p1msg2=await self.bot.wait_for(event="message", check=check2, timeout=10)
      except asyncio.TimeoutError:
        await channel1.send(lan["game"]["22"])
        await channel2.send(lan["game"]["18"])
        await asyncio.sleep(5)
        await channel1.delete()
        await channel2.delete()
        return
      else:
        try:
          p1atc=int(p1msg2.content)
        except:
          await channel1.send(lan["game"]["19"])
          await channel2.send(lan["game"]["18"])
          await asyncio.sleep(5)
          await channel1.delete()
          await channel2.delete()
          return
        else:
          if p1atc>25 or p1atc<1:
            await channel1.send(lan["game"]["19"])
            await channel2.send(lan["game"]["18"])
            await asyncio.sleep(5)
            await channel1.delete()
            await channel2.delete()
            return
      if p1atc==p2ship:
        await channel1.send(lan["game"]["23"])
        await channel2.send(lan["game"]["24"])
        if winner!="none":
          winner="even"
        else:
          winner="p1"
      else:
        await channel1.send(lan["game"]["25"])
        await channel2.send(lan["game"]["26"]+":"+str(p1atc))
        await channel2.send(lan["game"]["27"])
      
      await channel2.send(lan["game"]["20"])
      await channel1.send(lan["game"]["21"])

      try:
        p2msg2=await self.bot.wait_for(event="message", check=check3, timeout=10)
      except asyncio.TimeoutError:
        await channel2.send(lan["game"]["22"])
        await channel1.send(lan["game"]["18"])
        return
      else:
        try:
          p2atc=int(p2msg2.content)
        except:
          await channel1.send(lan["game"]["19"])
          await channel2.send(lan["game"]["18"])
          asyncio.sleep(5)
          await channel1.delete()
          await channel2.delete()
          return
        else:
          if p2atc>25 or p2atc<1:
            await channel2.send(lan["game"]["19"])
            await channel1.send(lan["game"]["18"])
            await asyncio.sleep(5)
            await channel1.delete()
            await channel2.delete()
            return
      if p2atc==p1ship:
        await channel2.send(lan["game"]["23"])
        await channel1.send(lan["game"]["24"])
        if winner!="none":
          winner="even"
        else:
          winner="p2"
      else:
        await channel2.send(lan["game"]["25"])
        await channel1.send(lan["game"]["26"]+":"+str(p2atc))
        await channel1.send(lan["game"]["27"])

      count+=1
      if winner!="none":
        break

    if winner=="none" or winner=="even":
      await channel1.send(lan["game"]["28"])
      await channel2.send(lan["game"]["28"])
    elif winner=="p1":
      await channel1.send(lan["game"]["29"])
      await channel2.send(lan["game"]["30"])
    elif winner=="p2":
      await channel1.send(lan["game"]["30"])
      await channel2.send(lan["game"]["29"])
    
    await asyncio.sleep(5)
    await channel1.delete()
    await channel2.delete()

    


def setup(bot):
    bot.add_cog(game(bot))