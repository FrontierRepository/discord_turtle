import discord
import json
import time
import datetime
import random
import requests
import asyncio
from discord.ext import commands
from core.classes import cog_extension
import core.inventory_func as inf

with open("./data/infor.json", mode="r", encoding="utf-8") as file:
  infor=json.load(file)

def take_cloud_data():
  response=requests.get("https://getpantry.cloud/apiv1/pantry/d214bda5-05ac-4723-8eb2-82176049788a/basket/CF")
  data=response.json()
  return data

def rewrite_cloud_data(data):
  update=requests.post("https://getpantry.cloud/apiv1/pantry/d214bda5-05ac-4723-8eb2-82176049788a/basket/CF",json=data)

def take_data():
  response=requests.get("https://getpantry.cloud/apiv1/pantry/d26176a1-04a8-42ce-a714-0e40e58b2801/basket/cute_turtle_currency")
  data=response.json()
  return data

def check_account(id, data):
  for x in data:
    if str(id) == x:
      return x
  return False 

def rewrite_data(data):
  update=requests.post("https://getpantry.cloud/apiv1/pantry/d26176a1-04a8-42ce-a714-0e40e58b2801/basket/cute_turtle_currency",json=data)

def search_user_in_guild(user, member_list):
  for member in member_list:
    if user == str(member)[:-5]:
      return member
  return False

def language(id):
  response=requests.get("https://getpantry.cloud/apiv1/pantry/01865685-19e7-4f85-9aa8-d8da22683475/basket/cute_turtle_guildinfo")
  gdif=response.json()

  with open("./data/localization_pack.json",mode="r",encoding="utf-8") as data:
    lanpak=json.load(data)

  for x in gdif:
    if x == str(id):
      lan=gdif[x]["lan"]
      return lanpak[lan]
  return lanpak["zhtw"]


inventory={"doggy":{"price":100,"func":inf.doggy}}

class currency(cog_extension):
  @commands.command()
  async def create(self,ctx):
    lan=language(ctx.guild.id)
    currency_data=take_data()
    for x in currency_data:
      if str(ctx.author.id) == x:
        await ctx.send(lan["currency"]["1"])
        return
    currency_data[ctx.author.id]={"money":0,"inventory":{},"last_work":"First"}
    rewrite_data(currency_data)
    await ctx.send(lan["currency"]["2"])
  #創建帳戶
  
  @commands.command()
  async def saving(self, ctx):
    lan=language(ctx.guild.id)
    currency_data=take_data()
    have_data=check_account(ctx.author.id,currency_data)
    if have_data != False:
      await ctx.send(lan["currency"]["3"]+str(currency_data[have_data]["money"])+lan["currency"]["4"])
      return
    await ctx.send(lan["currency"]["5"]+infor["prefix"]+lan["currency"]["6"])
  
  @commands.command()
  async def work(self,ctx):
    lan=language(ctx.guild.id)
    currency_data=take_data()
    have_account=check_account(ctx.author.id, currency_data)
    if have_account == False:
      await ctx.send(lan["currency"]["5"]+infor["prefix"]+lan["currency"]["6"])
      return
    
    now_time=datetime.datetime.now()
    
    if currency_data[have_account]["last_work"] == "First":
      random_num=random.uniform(100,400)
      salary=round(random_num)
      currency_data[have_account]["money"]+=salary
      await ctx.send(lan["currency"]["7"]+str(salary)+lan["currency"]["4"]+lan["currency"]["7.1"])
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
      await ctx.send(lan["currency"]["7"]+str(salary)+lan["currency"]["4"]+lan["currency"]["7.1"])
      now_unix_time=time.mktime(now_time.timetuple())
      currency_data[have_account]["last_work"]=now_unix_time
      rewrite_data(currency_data)
      return
    else:
      await ctx.send(lan["currency"]["8"])
    
  @commands.command()
  async def give(self ,ctx ,user_name, amount):
    lan=language(ctx.guild.id)
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
              await ctx.send(lan["currency"]["9"])
              return
            else:
              if give_total < 0:
                await ctx.send(lan["currency"]["10"])
                return
              if give_total>currency_data[have_account]["money"]:
                await ctx.send(lan["currency"]["11"])
                return
              currency_data[have_account]["money"]-=give_total
              currency_data[have_account2]["money"]+=give_total
              await ctx.send(lan["currency"]["12"]+amount+lan["currency"]["13"]+user_name)
              rewrite_data(currency_data)
              return
          else:
            await ctx.send(lan["currency"]["14"])
            return
        else:
          pass
      await ctx.send(lan["currency"]["15"])
      return
    await ctx.send(lan["currency"]["5"]+infor["prefix"]+lan["currency"]["6"])

  @commands.command()
  async def rob(self, ctx, user_name):
    lan=language(ctx.guild.id)
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
            await ctx.send(lan["currency"]["16"]+member2_name+lan["currency"]["17"]+str(get)+lan["currency"]["4"])
            rewrite_data(currency_data)
            return
          else:
            currency_data[have_account]["money"]-=500
            currency_data[have_account2]["money"]+=500
            if currency_data[have_account]["money"] < 0:
              currency_data[have_account]["money"]=0
            await ctx.send(lan["currency"]["18"]+member2_name+str(500)+lan["currency"]["4"])
            rewrite_data(currency_data)
            return
        else:
          await ctx.send(lan["currency"]["19"])
          return
      else:
        await ctx.send(lan["currency"]["15"])
        return
    else:
      await ctx.send(lan["currency"]["5"]+infor["prefix"]+lan["currency"]["6"])
  @commands.command()
  async def shop(self, ctx):
    lan=language(ctx.guild.id)
    embed=discord.Embed(title="SHOP", color=0x67ff5c)
    embed.add_field(name="doggy  100$", value=lan["currency"]["20"], inline=False)
    embed.set_footer(text=lan["currency"]["21"])
    await ctx.send(embed=embed)
  
  @commands.command()
  async def buy(self, ctx, stuff):
    lan=language(ctx.guild.id)
    currency_data=take_data()
    have_account=check_account(ctx.author.id,currency_data)
    if have_account == False:
      await ctx.send(lan["currency"]["5"]+infor["prefix"]+lan["currency"]["6"])
      return
    for x in inventory:
      if stuff == x:
        if inventory[x]["price"] > currency_data[have_account]["money"]:
          await ctx.send(lan["currency"]["22"])
          return
        for y in currency_data[have_account]["inventory"]:
          if y == stuff:
            currency_data[have_account]["inventory"][stuff]+=1
            currency_data[have_account]["money"]-=inventory[x]["price"]
            rewrite_data(currency_data)
            await ctx.send(lan["currency"]["23"])
            return
        currency_data[have_account]["inventory"][stuff]=1
        currency_data[have_account]["money"]-=inventory[x]["price"]
        rewrite_data(currency_data)
        await ctx.send(lan["currency"]["23"])
        return
    await ctx.send(lan["currency"]["24"])

  @commands.command()
  async def stuff(self, ctx, stuff):
    lan=language(ctx.guild.id)
    currency_data=take_data()
    have_account=check_account(ctx.author.id,currency_data)
    if have_account == False:
      await ctx.send(lan["currency"]["5"]+infor["prefix"]+lan["currency"]["6"])
      return
    for x in inventory:
      if stuff == x:
        for y in currency_data[have_account]["inventory"]:
          if stuff == y:
            if currency_data[have_account]["inventory"][stuff] == 0:
              await ctx.send(lan["currency"]["25"])
              return
            await ctx.send(lan["currency"]["26"]+str(currency_data[have_account]["inventory"][stuff])+lan["currency"]["27"]+stuff)
            return
        await ctx.send(lan["currency"]["25"])
        return
      await ctx.send(lan["currency"]["28"])

  @commands.command()
  async def inter(self, ctx, amount):
    lan=language(ctx.guild.id)
    data=take_data()
    cloud_data=take_cloud_data()
    money=int(amount)
    have_account=check_account(ctx.author.id,data)
    if have_account == False:
      await ctx.send(lan["currency"]["5"]+infor["prefix"]+lan["currency"]["6"])
      return
    if data[have_account]["money"]<=money+15:
      await ctx.send("您的帳戶存款不夠進行跨行轉帳")
      return
    data[have_account]["money"]=data[have_account]["money"]-money-15
    cloud_data["CtoF"][str(ctx.author.id)]=money
    rewrite_data(data)
    rewrite_cloud_data(cloud_data)
    await ctx.send("成功轉帳"+str(money)+"元(手續費15元)")

  @commands.command()
  async def use(self, ctx, stuff):
    lan=language(ctx.guild.id)
    data=take_data()
    have_account=check_account(ctx.author.id, data)
    if have_account == False:
      await ctx.send(lan["currency"]["5"]+infor["prefix"]+lan["currency"]["6"])
      return
    for x in inventory:
      if x == stuff:
        for y in data[have_account]["inventory"]:
          if data[have_account]["inventory"][y] <= 0:
            await ctx.send(lan["currency"]["25"])
            return
          await inventory[x]["func"](ctx)
          data[have_account]["inventory"][y]-=1
          rewrite_data(data)
          return
        await ctx.send(lan["currency"]["25"])
        return
      await ctx.send(lan["currency"]["28"])
    
  @commands.Cog.listener()
  async def on_message(self, msg):
    if ">>interbank" in msg.content:
      await asyncio.sleep(10)
      data=take_data()
      cloud_data=take_cloud_data()
      for x in cloud_data["FtoC"]:
        sucess=False
        for y in data:
          if x==y:
            data[y]["money"]=data[y]["money"]+cloud_data["FtoC"][x]
            success=True
        if success==False:
          cloud_data["CtoF"][x]=cloud_data["FtoC"][x]
      cloud_data["FtoC"]={}
      rewrite_data(data)
      rewrite_cloud_data(cloud_data)
          
    

        
    

    
    
def setup(bot):
  bot.add_cog(currency(bot))