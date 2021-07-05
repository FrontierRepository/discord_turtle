import discord
from discord.ext import commands
import json
import os
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

for Filename in os.listdir("./cmds"):
    if Filename.endswith(".py"):
        bot.load_extension("cmds."+str(Filename[:-3]))

if __name__ == "__main__":
    bot.run(infor["token"])