import discord
from discord.ext import commands
import json
import os
with open("./data/infor.json", mode="r", encoding="utf-8") as file:
  infor=json.load(file)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix=infor["prefix"], intents=intents)

bot.remove_command("help")


@bot.event
async def on_ready():
    print(">>>>>bot is starting to run<<<<<")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("8==D help"))
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
    await ctx.send("你還敢不把參數輸完整R")
  elif isinstance(ero, commands.errors.CommandNotFound):
    await ctx.send("你連個指令都能輸錯")
  elif isinstance(ero, commands.errors.MissingPermissions):
    await ctx.send("你缺少必要權限")
  else:
    await ctx.send("尛?")
    print(ero)
#在接收指令出問題時做出回應

@bot.group(invoke_without_command=True)
async def help(ctx):
  embed=discord.Embed(title="CUTE_TURTLE使用說明書", color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"help meme", value="查詢和迷因有關指令",inline=False)
  embed.add_field(name=infor["prefix"]+"help react", value="查詢和機器人搞~~人與人之間的連結~~,我是說互動的指令", inline=True)
  embed.add_field(name=infor["prefix"]+"help game", value="你確定要和我挑戰這些遊戲??", inline=False)
  embed.add_field(name=infor["prefix"]+"help currency", value="查詢有關邪惡的經濟系統的指令", inline=False)
  embed.add_field(name=infor["prefix"]+"help setting", value="查詢設定這隻機器人的指令", inline=False)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def meme(ctx):
  embed=discord.Embed(title="CUTE_TURTLE使用說明書-meme篇", color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"drDisrespect", value="跑出Dr.Disrespect的圖案", inline=False)
  embed.add_field(name=infor["prefix"]+"rick_roll", value="讓你切身體驗被rick roll的感覺", inline=True)
  embed.add_field(name=infor["prefix"]+"winnie", value="真可愛", inline=False)
  embed.add_field(name=infor["prefix"]+"knock_knock", value="有人進來了", inline=False)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def react(ctx):
  embed=discord.Embed(title="CUTE_TURTLE使用說明書-react篇", color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"hello", value="和你這個邊緣人say hello", inline=False)
  embed.add_field(name=infor["prefix"]+"delete [number]", value="剛剛傳了怪怪的訊息嗎?用這個刪掉吧(only能管理訊息的人可以用)", inline=False)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def setting(ctx):
  embed=discord.Embed(title="CUTE_TURTLE使用說明書-setting篇", color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"set_active_channel [channel id]", value="設定機器人平常跟你自動哈拉時要在哪裡哈拉", inline=True)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def game(ctx):
  embed=discord.Embed(title="CUTE_TURTLE使用說明書-game篇", color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"rps [your_choice]", value="和我這猜拳大師比簡直是個笑話(r=石頭 p=布 s=剪刀)", inline=False)
  embed.add_field(name=infor["prefix"]+"guess_meme", value="看你的迷因知識水準(全部英文小寫,空格請用_代替)" , inline=False)
  embed.add_field(name=infor["prefix"]+"war_ship", value="和其他人一同玩戰艦世界" , inline=False)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
@help.command()
async def currency(ctx):
  embed=discord.Embed(title="CUTE_TURTLE使用說明書-currency篇", color=0x67ff5c)
  embed.add_field(name=infor["prefix"]+"create", value="創建一個閃亮亮的全新帳戶", inline=False)
  embed.add_field(name=infor["prefix"]+"saving", value="看看你有多窮", inline=False)
  embed.add_field(name=infor["prefix"]+"work", value="當個免費勞工,領22K", inline=False)
  embed.add_field(name=infor["prefix"]+"give [user name] [amount]", value="公正,公平,公開der交易", inline=False)
  embed.add_field(name=infor["prefix"]+"rob", value="當個搶匪去搶錢,先說,你可能會被抓到", inline=False)
  embed.add_field(name=infor["prefix"]+"shop", value="幫你列出商品清單", inline=False)
  embed.add_field(name=infor["prefix"]+"buy [stuff]", value="買東西囉", inline=False)
  embed.set_footer(text="笑死,居然還需要幫忙")
  await ctx.send(embed=embed)
#更改預設的help指令

for Filename in os.listdir("./cmds"):
  if Filename.endswith(".py"):
    bot.load_extension("cmds."+str(Filename[:-3]))

if __name__ == "__main__":
  bot.run(infor["token"])