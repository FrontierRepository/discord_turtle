import discord
from discord.ext import commands
import json
with open("infor.json", mode="r") as file:
    infor=json.load(file)

bot=commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(">>>>>bot is starting to run<<<<<")
#確定機器人開始運行
@bot.event
async def on_member_join(member):
    print(f"{member} join")

@bot.event
async def on_member_remove(member):
    print(f"{member} leave")

bot.run(infor["token"])