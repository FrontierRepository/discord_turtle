import discord
from discord.ext import commands

from core.classes import cog_extension

class react(cog_extension):
    @commands.command()
    async def hello(self,ctx):
        await ctx.send("what's up sucker")
    #一個打招呼的指令

def setup(bot):
    bot.add_cog(react(bot))