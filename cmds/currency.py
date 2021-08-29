import discord
import json
import time
import datetime
import random
import requests
from discord.ext import commands
from core.classes import cog_extension

with open("./data/infor.json", mode="r", encoding="utf-8") as file:
  infor=json.load(file)

def take_cloud_data():
  response=requests.get("https://getpantry.cloud/apiv1/pantry/4feb1fac-6e16-4e25-9b43-12d4a2b7df5e/basket/discord_frontierguard")
  data=response.json()
  return data

def rewrite_cloud_data(data):
  update=requests.put("https://getpantry.cloud/apiv1/pantry/4feb1fac-6e16-4e25-9b43-12d4a2b7df5e/basket/discord_frontierguard",json=data)

def take_data():
  with open("./data/currency.json", mode="r", encoding="utf-8") as file:
    data=json.load(file)
  return data

def check_account(id, data):
  for x in data:
    if str(id) == x:
      return x
  return False 

def rewrite_data(data):
  with open("./data/currency.json", mode="w",encoding="utf-8") as file:
    json.dump(data,file)

def search_user_in_guild(user, member_list):
  for member in member_list:
    if user == str(member)[:-5]:
      return member
  return False

inventory={"doggy":100}

class currency(cog_extension):
  @commands.command()
  async def create(self,ctx):
    currency_data=take_data()
    for x in currency_data:
      if str(ctx.author.id) == x:
        await ctx.send("你已經創建過帳戶")
        return
    currency_data[ctx.author.id]={"money":0,"inventory":{},"last_work":"First"}
    rewrite_data(currency_data)
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
    how_long_have_been=now_time-last_time
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
    
  @commands.command()
  async def give(self ,ctx ,user_name, amount):
    currency_data=take_data()
    have_account=check_account(ctx.author.id, currency_data)
    if have_account != False:
      for member in ctx.guild.members:
        if user_name == str(member)[:-5]:
          have_account2=check_account(member.id, currency_data)
          if have_account2 != False:
            try:
              give_total=int(amount)
            except:
              await ctx.send("啥時有這種數字了?")
              return
            else:
              if give_total < 0:
                await ctx.send("我不吃負數這套")
                return
              if give_total>currency_data[have_account]["money"]:
                await ctx.send("你太窮了,交易不了")
                return
              currency_data[have_account]["money"]-=give_total
              currency_data[have_account2]["money"]+=give_total
              await ctx.send("成功交易"+amount+"元給"+user_name)
              rewrite_data(currency_data)
              return
          else:
            await ctx.send("對方尚未創建帳戶")
            return
        else:
          pass
      await ctx.send("這誰?")
      return
    await ctx.send("你尚未創建帳戶,輸入"+infor["prefix"]+"create來創建")

  @commands.command()
  async def rob(self, ctx, user_name):
    currency_data=take_data()
    have_account=check_account(ctx.author.id,currency_data)
    if have_account != False:
      have_member=search_user_in_guild(user_name, ctx.guild.members)
      if have_member != False:
        have_account2=check_account(have_member.id,currency_data)
        if have_account2 != False:
          member2_name=str(have_member)[:-5]
          chance=random.uniform(1,10)
          if chance >= 6:
            randomF=random.uniform(300,700)
            get=round(randomF)
            currency_data[have_account]["money"]+=get
            currency_data[have_account2]["money"]-=get
            if currency_data[have_account2]["money"] < 0:
              currency_data[have_account2]["money"]=0
            await ctx.send("你成功從"+member2_name+"身上搶了"+str(get)+"元")
            rewrite_data(currency_data)
            return
          else:
            currency_data[have_account]["money"]-=500
            currency_data[have_account2]["money"]+=500
            if currency_data[have_account]["money"] < 0:
              currency_data[have_account]["money"]=0
            await ctx.send("你被抓到了,並且賠償"+member2_name+"500元")
            rewrite_data(currency_data)
            return
        else:
          await ctx.send("對方沒帳戶給你搶")
          return
      else:
        await ctx.send("這誰?")
        return
    else:
      await ctx.send("你尚未創建帳戶,輸入"+infor["prefix"]+"create來創建")
  @commands.command()
  async def shop(self, ctx):
    embed=discord.Embed(title="SHOP", color=0x67ff5c)
    embed.add_field(name="doggy  100$", value="一直可愛但沒啥用的狗勾", inline=False)
    embed.set_footer(text="今天沒有特價ㄏㄏ")
    await ctx.send(embed=embed)
  
  @commands.command()
  async def buy(self, ctx, stuff):
    currency_data=take_data()
    have_account=check_account(ctx.author.id,currency_data)
    if have_account == False:
      await ctx.send("你尚未創建帳戶,輸入"+infor["prefix"]+"create來創建")
      return
    for x in inventory:
      if stuff == x:
        if inventory[x] > currency_data[have_account]["money"]:
          await ctx.send("你太窮了,買不起")
          return
        for y in currency_data[have_account]["inventory"]:
          if y == stuff:
            currency_data[have_account]["inventory"][stuff]+=1
            currency_data[have_account]["money"]-=inventory[x]
            rewrite_data(currency_data)
            await ctx.send("購買成功")
            return
        currency_data[have_account]["inventory"][stuff]=1
        currency_data[have_account]["money"]-=inventory[x]
        rewrite_data(currency_data)
        await ctx.send("購買成功")
        return
    await ctx.send("這啥?")

  @commands.command()
  async def stuff(self, ctx, stuff):
    currency_data=take_data()
    have_account=check_account(ctx.author.id,currency_data)
    if have_account == False:
      await ctx.send("你尚未創建帳戶,輸入"+infor["prefix"]+"create來創建")
      return
    for x in inventory:
      if stuff == x:
        for y in currency_data[have_account]["inventory"]:
          if stuff == y:
            if currency_data[have_account]["inventory"][stuff] == 0:
              await ctx.send("你沒有這個東西")
              return
            await ctx.send("你有"+str(currency_data[have_account]["inventory"][stuff])+"個"+stuff)
            return
        await ctx.send("你沒有這個東西")
        return
      await ctx.send("有這東西?")
        
    

    
    
def setup(bot):
  bot.add_cog(currency(bot))