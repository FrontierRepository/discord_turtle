import discord
import json
import time
import datetime
import random
from discord.ext import commands
from core.classes import cog_extension

with open("infor.json", mode="r", encoding="utf-8") as file:
  infor=json.load(file)

def take_data():
  with open("currency.json", mode="r", encoding="utf-8") as file:
    data=json.load(file)
  return data

def check_account(id, data):
  for x in data:
    if str(id) == x:
      return x
  return False 

def rewrite_data(data):
  with open("currency.json", mode="w",encoding="utf-8") as file:
    json.dump(data,file)

class currency(cog_extension):
  @commands.command()
  async def create(self,ctx):
    currency_data=take_data()
    for x in currency_data:
      if str(ctx.author.id) == x:
        await ctx.send("你已經創建過帳戶")
        return
    currency_data[ctx.author.id]={"money":0,"inventory":{},"last_work":"First"}
    with open("currency.json", mode="w", encoding="utf-8") as file:
      json.dump(currency_data, file)
    await ctx.send("帳戶創建成功")
  #創建帳戶
  
  @commands.command()
  async def saving(self, ctx):
    currency_data=take_data()
    have_data=check_account(ctx.author.id,currency_data)
    if have_data != False:
      await ctx.send("你的帳戶有"+str(currency_data[have_data]["money"])+"元")
      return
    await ctx.send("你尚未創建帳戶,輸入"+infor["prefix"]+"create來創建帳戶")
  
  @commands.command()
  async def work(self,ctx):
    currency_data=take_data()
    have_account=check_account(ctx.author.id, currency_data)
    if have_account == False:
      await ctx.send("你尚未創建帳戶,輸入"+infor["prefix"]+"create來創建帳戶")
      return
    
    now_time=datetime.datetime.now()
    
    if currency_data[have_account]["last_work"] == "First":
      random_num=random.uniform(100,400)
      salary=round(random_num)
      currency_data[have_account]["money"]+=salary
      await ctx.send("你在工作中得到了"+str(salary)+"元")
      now_unix_time=time.mktime(now_time.timetuple())
      currency_data[have_account]["last_work"]=now_unix_time
      rewrite_data(currency_data)
      return
    
    last_time=datetime.datetime.fromtimestamp(currency_data[have_account]["last_work"])
    how_long_have_been=last_time-now_time
    thirty_minutes=datetime.timedelta(
      minutes=30
    )

    if how_long_have_been>=thirty_minutes:
      random_num=random.uniform(100,400)
      salary=round(random_num)
      currency_data[have_account]["money"]+=salary
      await ctx.send("你在工作中得到了"+str(salary)+"元")
      now_unix_time=time.mktime(now_time.timetuple())
      currency_data[have_account]["last_work"]=now_unix_time
      rewrite_data(currency_data)
      return
    else:
      await ctx.send("修但幾列,你剛剛才工作ㄟ")

    
    
def setup(bot):
  bot.add_cog(currency(bot))