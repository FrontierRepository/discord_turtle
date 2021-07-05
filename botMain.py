import discord
from discord.ext import commands
import json
import os
import keep_alive
with open("infor.json", mode="r", encoding="utf-8") as file:
    infor=json.load(file)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="8==D ", intents=intents)

@bot.event
async def on_ready():
    print(">>>>>bot is starting to run<<<<<")
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
  if isinstance(ero, commands.errors.MissingRequiredArgument):
    await ctx.send("你這傻B還敢不輸完整R")
  elif isinstance(ero, commands.errors.CommandNotFound):
    await ctx.send("你連個指令都能輸錯")
  else:
    await ctx.send("尛?")

for Filename in os.listdir("./cmds"):
    if Filename.endswith(".py"):
        bot.load_extension("cmds."+str(Filename[:-3]))

if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(infor["token"])