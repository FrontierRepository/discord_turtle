import discord
from discord.ext import commands
import json
with open("infor.json", mode="r", encoding="utf-8") as file:
    infor=json.load(file)

from core.classes import cog_extension

class meme(cog_extension):
    @commands.command()
    async def rick_roll(self, ctx):
        await ctx.send(infor["rick_roll"])
    #一個rick roll別人的指令

    @commands.command()
    async def drDisrespect(self, ctx):
        await ctx.send(infor["drDis"])
    #一個會出現Dr.disrespect的指令

def setup(bot):
    bot.add_cog(meme(bot))