import discord
from discord.ext import commands
import json
with open("infor.json", mode="r") as file:
    infor = json.load(file)

bot=commands.Bot(command_prefix="8==D")
print(infor["token"])
