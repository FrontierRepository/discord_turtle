import discord
from discord.ext import commands
import json
import os
import keep_alive
with open("infor.json", mode="r", encoding="utf-8") as file:
    infor=json.load(file)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix=infor["prefix"], intents=intents)

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
  embed.add_field(name=infor["prefix"]+"help meme", value="查詢和迷因有關指令",inline=False)
  embed.add_field(name=infor["prefix"]+"help react", value="查詢和機器人搞~~人與人之間的連結~~,我是說互動的指令", inline=True)
  embed.add_field(name=infor["prefix"]+"help game", value="你確定要和我挑戰這些遊戲??", inline=False)
  embed.add_field(name=infor["prefix"]+"help setting", value="查詢設定這隻機器人的指令", inline=False)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def meme(ctx):
  await ctx.channel.purge(limit=1)
  embed=discord.Embed(title="CUTE_TURTLE使用說明書-meme篇", color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"drDisrespect", value="跑出Dr.Disrespect的圖案", inline=False)
  embed.add_field(name=infor["prefix"]+"rick_roll", value="讓你切身體驗被rick roll的感覺", inline=True)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def react(ctx):
  await ctx.channel.purge(limit=1)
  embed=discord.Embed(title="CUTE_TURTLE使用說明書-react篇", color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"hello", value="和你這個邊緣人say hello", inline=False)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def setting(ctx):
  await ctx.channel.purge(limit=1)
  embed=discord.Embed(title="CUTE_TURTLE使用說明書-setting篇", color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"set_active_channel [channel id]", value="設定機器人平常跟你自動哈拉時要在哪裡哈拉", inline=True)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def game(ctx):
  await ctx.channel.purge(limit=1)
  embed=discord.Embed(title="CUTE_TURTLE使用說明書-game篇", color=0x67ff5c)
  embed.add_field(name="8==D rps [your_choice]", value="和我這猜拳大師比簡直是個笑話(r=石頭 p=布 s=剪刀)", inline=False)
  embed.add_field(name=infor["prefix"]+"guess_meme", value="看你的迷因知識水準(全部英文小寫,空格請用_代替)" , inline=False)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
#更改預設的help指令

for Filename in os.listdir("./cmds"):
    if Filename.endswith(".py"):
        bot.load_extension("cmds."+str(Filename[:-3]))

if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(infor["token"])