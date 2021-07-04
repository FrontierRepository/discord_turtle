import discord
from discord.ext import commands
import json
with open("infor.json", mode="r") as file:
    infor=json.load(file)

bot=commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(">>>>>bot is starting to run<<<<<")

bot.run(infor["token"])