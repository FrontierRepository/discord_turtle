import discord
from discord.ext import commands
import json
import os
import keep_alive
with open("infor.json", mode="r", encoding="utf-8") as file:
    infor=json.load(file)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="8==D ", intents=intents)

bot.remove_command("help")

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
#在接收指令出問題時做出回應

@bot.group()
async def help(ctx):
  embed=discord.Embed(title="CUTE_TURTLE使用說明書", color=0x67ff5c)
  embed.add_field(name="8==D help meme", value="查詢和迷因有關指令",inline=False)
  embed.add_field(name="8==D help react", value="查詢其他的指令", inline=True)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def meme(ctx):
  await ctx.channel.purge(limit=1)
  embed=discord.Embed(title="CUTE_TURTLE使用說明書-meme篇", color=0x67ff5c)
  embed.add_field(name="8==D drDisrespect", value="跑出Dr.Disrespect的圖案", inline=False)
  embed.add_field(name="8==D rick_roll", value="讓你切身體驗被rick roll的感覺", inline=True)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def react(ctx):
  await ctx.channel.purge(limit=1)
  embed=discord.Embed(title="CUTE_TURTLE使用說明書-react篇", color=0x67ff5c)
  embed.add_field(name="8==D hello", value="和你這個邊緣人say hello", inline=False)
  embed.add_field(name="8==D rps [your_choice]", value="和我這猜拳大師比簡直是個笑話(r=石頭 p=布 s=剪刀)", inline=False)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
#更改預設的help指令

for Filename in os.listdir("./cmds"):
    if Filename.endswith(".py"):
        bot.load_extension("cmds."+str(Filename[:-3]))

if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(infor["token"])