import discord
import json
from discord.ext import commands
from core.classes import cog_extension

class event(cog_extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):  
        with open("./data/guildinfo.json", mode="r",encoding="utf-8") as file:
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
      with open("./data/guildinfo.json", mode="r",encoding="utf-8") as file:
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
        if "https://www.youtube.com/watch?v=dQw4w9WgXcQ" in msg.content or "https://www.youtube.com/watch?v=xvFZjo5PgG0" in msg.content or "https://www.youtube.com/watch?v=QtBDL8EiNZo&t=15s" in msg.content or "www.tomorrowtides.com" in msg.content  or "http://www.lasesp.com/article/" in msg.content or "https://rr.noordstar.me" in msg.content and msg.author!=self.bot.user:
          await msg.channel.send("!!!警告!!!這可能是rick roll")
        
        if msg.content=="安安" and msg.guild.id==881108501915635714:
          await msg.channel.send("安屁安阿")
    #在偵測到特定訊息時回復

def setup(bot):
    bot.add_cog(event(bot))