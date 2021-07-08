import discord
import random
import asyncio
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


def setup(bot):
    bot.add_cog(react(bot))