import discord
import random
import asyncio
import json
import os

from discord.ext import commands

from core.classes import cog_extension


for filename in os.listdir("./cmds"):
  if filename == "meme.json":
      with open("data."+str(filename) ,mode="r",encoding="utf-8") as file:
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

class game(cog_extension):
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
    await ctx.send("這是哪個迷因")
    await ctx.send(meda[self.ans])

    def check(m):
      return m.content==str(self.ans) and m.channel==ctx.channel and m.author==ctx.author
      
    try:
      self.msg=await self.bot.wait_for(event="message",check=check, timeout=25)
    except asyncio.TimeoutError:
      await ctx.send("超時了你這SB,答案是"+self.ans)
    else:
      await ctx.send("正確答案")
    #玩猜迷因的指令
  
  @commands.command()
  async def war_ship(self,ctx):
    with open("./data/infor.json" ,mode="r",encoding="utf-8") as file:
      infor=json.load(file)

    user1=ctx.author
    await ctx.send("等待配對,輸入+1來加入")
    def check(m):
      return m.content=="+1" and m.author!=ctx.author and m.channel==ctx.channel
    try:
      msg=await self.bot.wait_for(event="message", check=check, timeout=30)
    except asyncio.TimeoutError:
      await ctx.send("看來你太邊緣了")
      return
    else:
      await ctx.send("配對成功")
      await ctx.send("對手:"+str(msg.author))
    user2=msg.author

    channel1=await ctx.guild.create_text_channel("player1")
    channel2=await ctx.guild.create_text_channel("player2")
    for role in ctx.guild.roles:
      if role.name=="@everyone":
        await channel1.set_permissions(role,view_channel=False)
        await channel2.set_permissions(role,view_channel=False)

    for member in ctx.guild.members:
      if member==user1:
        await channel1.set_permissions(member,view_channel=True)
      if member==user2:
        await channel2.set_permissions(member,view_channel=True)
    
    await channel1.send("遊戲開始")
    await channel2.send("遊戲開始")
    await channel1.send(infor["25"])
    await channel2.send(infor["25"])
    await channel1.send("請選擇船艦擺設的位置")
    await channel2.send("等待對方放置船隻")

    def check2(m):
      return m.channel==channel1
    
    try:
      p1msg=await self.bot.wait_for(event="message", check=check2, timeout=10)
    except asyncio.TimeoutError:
      await channel1.send("等待過久,你棄權了")
      await channel2.send("對方棄權了")
      return
    else:
      try:
        p1ship=int(p1msg.content)
      except:
        await channel1.send("輸入格式錯誤,你棄權了")
        await channel2.send("對方棄權了")
        asyncio.sleep(5)
        await channel1.delete()
        await channel2.delete()
        return
      else:
        if p1ship>25 or p1ship<1:
          await channel1.send("輸入格式錯誤,你棄權了")
          await channel2.send("對方棄權了")
          await asyncio.sleep(5)
          await channel1.delete()
          await channel2.delete()
          return
    
    await channel2.send("請選擇船艦擺設的位置")
    await channel1.send("等待對方放置船隻")

    def check3(m):
      return m.channel==channel2
    try:
      p2msg=await self.bot.wait_for(event="message", check=check3, timeout=10)
    except asyncio.TimeoutError:
      await channel2.send("等待過久,你棄權了")
      await channel1.send("對方棄權了")
      await asyncio.sleep(5)
      await channel1.delete()
      await channel2.delete()
      return
    else:
      try:
        p2ship=int(p2msg.content)
      except:
        await channel1.send("輸入格式錯誤,你棄權了")
        await channel2.send("對方棄權了")
        asyncio.sleep(5)
        await channel1.delete()
        await channel2.delete()
        return
      else:
        if p2ship>25 or p2ship<1:
          await channel2.send("輸入格式錯誤,你棄權了")
          await channel1.send("對方棄權了")
          await asyncio.sleep(5)
          await channel1.delete()
          await channel2.delete()
          return

    count=0
    winner="none"
    while count<10:
      await channel1.send("請選擇要攻擊的位置")
      await channel2.send("等待對方攻擊")

      try:
        p1msg2=await self.bot.wait_for(event="message", check=check2, timeout=10)
      except asyncio.TimeoutError:
        await channel1.send("等待過久,你棄權了")
        await channel2.send("對方棄權了")
        await asyncio.sleep(5)
        await channel1.delete()
        await channel2.delete()
        return
      else:
        try:
          p1atc=int(p1msg2.content)
        except:
          await channel1.send("輸入格式錯誤,你棄權了")
          await channel2.send("對方棄權了")
          asyncio.sleep(5)
          await channel1.delete()
          await channel2.delete()
          return
        else:
          if p1atc>25 or p1atc<1:
            await channel1.send("輸入格式錯誤,你棄權了")
            await channel2.send("對方棄權了")
            await asyncio.sleep(5)
            await channel1.delete()
            await channel2.delete()
            return
      if p1atc==p2ship:
        await channel1.send("擊中")
        await channel2.send("對方成功擊中")
        if winner!="none":
          winner="even"
        else:
          winner="p1"
      else:
        await channel1.send("失誤")
        await channel2.send("對方攻擊:"+str(p1atc))
        await channel2.send("對方失誤")
      
      await channel2.send("請選擇要攻擊的位置")
      await channel1.send("等待對方攻擊")

      try:
        p2msg2=await self.bot.wait_for(event="message", check=check3, timeout=10)
      except asyncio.TimeoutError:
        await channel2.send("等待過久,你棄權了")
        await channel1.send("對方棄權了")
        return
      else:
        try:
          p2atc=int(p2msg2.content)
        except:
          await channel1.send("輸入格式錯誤,你棄權了")
          await channel2.send("對方棄權了")
          asyncio.sleep(5)
          await channel1.delete()
          await channel2.delete()
          return
        else:
          if p2atc>25 or p2atc<1:
            await channel2.send("輸入格式錯誤,你棄權了")
            await channel1.send("對方棄權了")
            await asyncio.sleep(5)
            await channel1.delete()
            await channel2.delete()
            return
      if p2atc==p1ship:
        await channel2.send("擊中")
        await channel1.send("對方成功擊中")
        if winner!="none":
          winner="even"
        else:
          winner="p2"
      else:
        await channel2.send("失誤")
        await channel1.send("對方攻擊:"+str(p2atc))
        await channel1.send("對方失誤")

      count+=1
      if winner!="none":
        break

    if winner=="none" or winner=="even":
      await channel1.send("平手")
      await channel2.send("平手")
    elif winner=="p1":
      await channel1.send("勝利")
      await channel2.send("失敗")
    elif winner=="p2":
      await channel1.send("失敗")
      await channel2.send("勝利")
    
    await asyncio.sleep(5)
    await channel1.delete()
    await channel2.delete()

    


def setup(bot):
    bot.add_cog(game(bot))