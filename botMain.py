import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(">>>>>bot is starting to run<<<<<")

bot.run("ODQ2OTMyODIxMzk3OTk1NTQw.YK2tpw.dpljs9bVdbr0nD4rdVRpo6Wbdqk")