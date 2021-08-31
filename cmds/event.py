import discord
import json
import cv2 as cv
import numpy as np
import os
import requests
from discord.ext import commands
from core.classes import cog_extension

def rescale(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    hieght = int(frame.shape[0]*scale)
    dimensions = (width, hieght)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

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

class event(cog_extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):  
        with open("./data/guildinfo.json", mode="r",encoding="utf-8") as file:
          gdata=json.load(file)
        
        mg=member.guild.id

        img=cv.imread("./img/mickeysuicide.jpg")
        cv.putText(img, "welcome "+member.name, (0,50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,225,100), 1)
        cv.imwrite("./img/output.jpg",img)
        file=discord.File("./img/output.jpg")
        
        for x in gdata:
          if str(mg)==x:
            if gdata[x]["id"] != "None":
              channel = self.bot.get_channel(gdata[x]["id"])
        
        await channel.send(">>"+str(member)+" join!")
        await channel.send(file=file)
        
        os.remove("./img/output.jpg")
    #在成員加入時發送訊息
    @commands.Cog.listener()
    async def on_member_remove(self, member):
      with open("./data/guildinfo.json", mode="r",encoding="utf-8") as file:
          gdata=json.load(file)
        
      mg=member.guild.id

      for x in gdata:
        if str(mg)==x:
          if gdata[x]["id"] != "None":
            channel = self.bot.get_channel(gdata[x]["id"])

      await channel.send(">>"+str(member)+" leave!")
    #在成員離開時發送訊息

    @commands.Cog.listener()
    async def on_message(self, msg):
      lan=language(msg.guild.id)
      if "https://www.youtube.com/watch?v=dQw4w9WgXcQ" in msg.content or "https://www.youtube.com/watch?v=xvFZjo5PgG0" in msg.content or "https://www.youtube.com/watch?v=QtBDL8EiNZo&t=15s" in msg.content or "www.tomorrowtides.com" in msg.content  or "http://www.lasesp.com/article/" in msg.content or "https://rr.noordstar.me" in msg.content and msg.author!=self.bot.user:
        await msg.channel.send(lan["event"]["1"])
        
      if msg.content=="安安" and msg.guild.id==881108501915635714:
        await msg.channel.send("安屁安阿")
    #在偵測到特定訊息時回復

def setup(bot):
    bot.add_cog(event(bot))