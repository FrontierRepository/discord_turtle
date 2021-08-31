import discord
import json
from discord.ext import commands
from core.classes import cog_extension

language_list=("zhtw","en")

def language(id):
  with open("./data/guildinfo.json",mode="r",encoding="utf-8") as file:
    gdif=json.load(file)

  with open("./data/localization_pack.json",mode="r",encoding="utf-8") as data:
    lanpak=json.load(data)

  for x in gdif:
    if x == str(id):
      lan=gdif[x]["lan"]
      return lanpak[lan]
  return lanpak["zhtw"]

class setting(cog_extension):
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def set_active_channel(self, ctx, cid):
    with open("./data/guildinfo.json", mode="r", encoding="utf-8") as file:
       gdata=json.load(file)
    have_data=False
    for x in gdata:
      if x==str(ctx.guild.id):
        have_data=True
        if cid=="0":
          gdata[str(ctx.guild.id)]["id"]="None"
        else:
          gdata[str(ctx.guild.id)]["id"]=int(cid)

    if have_data==False:
      gdata[str(ctx.guild.id)]={"id":int(cid),"lan":"zhtw"}

    with open("./data/guildinfo.json", mode="w", encoding="utf-8") as file:
      json.dump(gdata, file)
    if cid == "0":
      await ctx.send("successfully cancel the active channel")
    else:
      await ctx.send("successfully change active channel into " +cid)
  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def language(self, ctx, lan):
    pack=language(ctx.guild.id)
    with open("./data/guildinfo.json",mode="r",encoding="utf-8") as file:
      data=json.load(file)
    
    have_account=False

    for x in data:
      have_account=True
      if x==str(ctx.guild.id):
        if lan in language_list:
          data[str(ctx.guild.id)]["lan"]=lan
          await ctx.send(pack["setting"]["1"])
        else:
          await ctx.send(pack["setting"]["2"])

    if have_account==False:
      data[str(ctx.guild.id)]={"id":"None","lan":lan}

    with open("./data/guildinfo.json", mode="w", encoding="utf-8") as file:
      json.dump(data, file)

def setup(bot):
  bot.add_cog(setting(bot))