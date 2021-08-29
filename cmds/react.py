import discord
import random
import asyncio
import sys
import requests
import json
from discord.ext import commands

from core.classes import cog_extension

class react(cog_extension):
    @commands.command()
    async def hello(self,ctx):
        await ctx.send("what's up sucker")
    #一個打招呼的指令

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def delete(self,ctx,num):
      await ctx.channel.purge(limit=int(num)+1)
      await ctx.send("已刪除"+num+"則訊息")
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
      response=requests.get("https://getpantry.cloud/apiv1/pantry/4feb1fac-6e16-4e25-9b43-12d4a2b7df5e/basket/discord_frontierguard")

      data=response.json()
      print(data["record"])

      data["disisnew"]="see_its_new"

      update=requests.put("https://getpantry.cloud/apiv1/pantry/4feb1fac-6e16-4e25-9b43-12d4a2b7df5e/basket/discord_frontierguard",json=data)

      print(update)



def setup(bot):
    bot.add_cog(react(bot))