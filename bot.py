import discord
from discord.ext import commands
import json
import os
import requests
with open("./data/infor.json", mode="r", encoding="utf-8") as file:
  infor=json.load(file)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix=infor["prefix"], intents=intents)

bot.remove_command("help")

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

@bot.event
async def on_ready():
    print(">>>>>bot is starting to run<<<<<")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(infor["prefix"]"help"))
#確認機器人開始運作

@bot.command()
async def load(ctx, extension):
    bot.load_extension("cmds."+str(extension))
    await ctx.send("successfully loaded")
#load cog

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension("cmds."+str(extension))
    await ctx.send("successfully unloaded")
#unload cog

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension("cmds."+str(extension))
    await ctx.send("successfully reloaded")
#reload cog

@bot.event
async def on_command_error(ctx, ero):
  lan=language(ctx.guild.id)
  if isinstance(ero, commands.errors.MissingRequiredArgument):
    await ctx.send(lan["main"]["1"])
  elif isinstance(ero, commands.errors.CommandNotFound):
    await ctx.send(lan["main"]["2"])
  elif isinstance(ero, commands.errors.MissingPermissions):
    await ctx.send(lan["main"]["3"])
  else:
    await ctx.send(lan["main"]["4"])
    print(ero)
#在接收指令出問題時做出回應

@bot.group(invoke_without_command=True)
async def help(ctx):
  lan=language(ctx.guild.id)
  embed=discord.Embed(title=lan["main"]["5"], color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"help meme", value=lan["main"]["6"],inline=False)
  embed.add_field(name=infor["prefix"]+"help react", value=lan["main"]["7"], inline=True)
  embed.add_field(name=infor["prefix"]+"help game", value=lan["main"]["8"], inline=False)
  embed.add_field(name=infor["prefix"]+"help currency", value=lan["main"]["9"], inline=False)
  embed.add_field(name=infor["prefix"]+"help setting", value=lan["main"]["10"], inline=False)
  embed.set_footer(text=lan["main"]["11"])
  await ctx.send(embed=embed)
@help.command()
async def meme(ctx):
  lan=language(ctx.guild.id)
  embed=discord.Embed(title=lan["main"]["12"], color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"drDisrespect", value=lan["main"]["13"], inline=False)
  embed.add_field(name=infor["prefix"]+"rick_roll", value=lan["main"]["14"], inline=True)
  embed.add_field(name=infor["prefix"]+"knock_knock", value=lan["main"]["16"], inline=False)
  embed.set_footer(text=lan["main"]["11"])
  await ctx.send(embed=embed)
@help.command()
async def react(ctx):
  lan=language(ctx.guild.id)
  embed=discord.Embed(title=lan["main"]["17"], color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"hello", value=lan["main"]["18"], inline=False)
  embed.add_field(name=infor["prefix"]+"delete [number]", value=lan["main"]["19"], inline=False)
  embed.set_footer(text=lan["main"]["11"])
  await ctx.send(embed=embed)
@help.command()
async def setting(ctx):
  lan=language(ctx.guild.id)
  embed=discord.Embed(title=lan["main"]["20"], color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"set_active_channel [channel id]", value=lan["main"]["21"], inline=False)
  embed.add_field(name=infor["prefix"]+"language [language]", value=lan["main"]["22"]+":zhtw,en",inline=False)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def game(ctx):
  lan=language(ctx.guild.id)
  embed=discord.Embed(title=lan["main"]["24"], color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"rps [your_choice]", value=lan["main"]["25"], inline=False)
  embed.add_field(name=infor["prefix"]+"guess_meme", value=lan["main"]["26"] , inline=False)
  embed.add_field(name=infor["prefix"]+"war_ship", value=lan["main"]["27"] , inline=False)
  embed.set_footer(text=lan["main"]["11"])
  await ctx.send(embed=embed)
@help.command()
async def currency(ctx):
  lan=language(ctx.guild.id)
  embed=discord.Embed(title=lan["main"]["28"], color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"create", value=lan["main"]["29"], inline=False)
  embed.add_field(name=infor["prefix"]+"saving", value=lan["main"]["30"], inline=False)
  embed.add_field(name=infor["prefix"]+"work", value=lan["main"]["31"], inline=False)
  embed.add_field(name=infor["prefix"]+"give [user name] [amount]", value=lan["main"]["32"], inline=False)
  embed.add_field(name=infor["prefix"]+"rob", value=lan["main"]["33"], inline=False)
  embed.add_field(name=infor["prefix"]+"shop", value=lan["main"]["34"], inline=False)
  embed.add_field(name=infor["prefix"]+"buy [stuff]", value=lan["main"]["35"], inline=False)
  embed.add_field(name=infor["prefix"]+"use [stuff]", value=lan["main"]["36"], inline=False)
  embed.set_footer(text=lan["main"]["11"])
  await ctx.send(embed=embed)
#更改預設的help指令

for Filename in os.listdir("./cmds"):
  if Filename.endswith(".py"):
    bot.load_extension("cmds."+str(Filename[:-3]))

if __name__ == "__main__":
  bot.run(infor["token"])