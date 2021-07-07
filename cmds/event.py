import discord
import json
from discord.ext import commands
from core.classes import cog_extension

class event(cog_extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):  
        with open("guildinfo.json", mode="r",encoding="utf-8") as file:
          gdata=json.load(file)
        
        mg=member.guild.id
        
        for x in gdata:
          if str(mg)==x:
            if gdata[x]!= "None":
              channel = self.bot.get_channel(gdata[x])
        
        await channel.send(">>"+str(member)+" join!")
    #在成員加入時發送訊息
    @commands.Cog.listener()
    async def on_member_remove(self, member):
      with open("guildinfo.json", mode="r",encoding="utf-8") as file:
          gdata=json.load(file)
        
      mg=member.guild.id

      for x in gdata:
        if str(mg)==x:
          if gdata[x]!= "None":
            channel = self.bot.get_channel(gdata[x])

      await channel.send(">>"+str(member)+" leave!")
    #在成員離開時發送訊息

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg == "you know the rules":
            await msg.channel.send("and so do I")
    #在偵測到特定訊息時回復

def setup(bot):
    bot.add_cog(event(bot))