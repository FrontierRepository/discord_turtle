import discord
from discord.ext import commands
import json
import os
with open("infor.json", mode="r", encoding="utf8") as file:
    infor=json.load(file)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="8==D ", intents=intents)

@bot.event
async def on_ready():
    print(">>>>>bot is starting to run<<<<<")
#確認機器人開始運作

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(860469237214740491)
    await channel.send(">>"+str(member)+" join!")
#在成員加入時發送訊息

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(860469237214740491)
    await channel.send(">>"+str(member)+" leave!")
#在成員離開時發送訊息

@bot.command()
async def load(ctx, extension):
    bot.load_extension("cmds."+str(extension))
    await ctx.send("successfully loaded")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension("cmds."+str(extension))
    await ctx.send("successfully unloaded")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension("cmds."+str(extension))
    await ctx.send("successfully reloaded")

for Filename in os.listdir("./cmds"):
    if Filename.endswith(".py"):
        bot.load_extension("cmds."+str(Filename[:-3]))

if __name__ == "__main__":
    bot.run(infor["token"])