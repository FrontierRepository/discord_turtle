import discord
from discord.ext import commands
import json
with open("infor.json", mode="r") as file:
    infor=json.load(file)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(">>>>>bot is starting to run<<<<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(860469237214740491)
    await channel.send(">>"+str(member)+" join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(860469237214740491)
    await channel.send(">>"+str(member)+" leave!")

bot.run(infor["token"])