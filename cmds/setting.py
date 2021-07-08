import discord
import json
from discord.ext import commands
from core.classes import cog_extension

class setting(cog_extension):
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def set_active_channel(self, ctx, cid):
    with open("guildinfo.json", mode="r", encoding="utf-8") as file:
       gdata=json.load(file)
    if cid=="0":
      gdata[str(ctx.guild.id)]="None"
    else:
      gdata[str(ctx.guild.id)]=int(cid)
    with open("guildinfo.json", mode="w", encoding="utf-8") as file:
      json.dump(gdata, file)
    if cid == "0":
      await ctx.send("successfully cancel the active channel")
    else:
      await ctx.send("successfully change active channel into " +cid)
    
def setup(bot):
  bot.add_cog(setting(bot))