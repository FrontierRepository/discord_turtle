import discord
from discord.ext import commands
import requests
import json
import asyncio
import time
import datetime
import random

def take_data():
  response=requests.get("https://getpantry.cloud/apiv1/pantry/d26176a1-04a8-42ce-a714-0e40e58b2801/basket/cute_turtle_currency")
  data=response.json()
  return data

async def rewrite_data(data):
  update=requests.post("https://getpantry.cloud/apiv1/pantry/d26176a1-04a8-42ce-a714-0e40e58b2801/basket/cute_turtle_currency",json=data)
  print(update)

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

def search_user_in_guild(user, member_list):
  for member in member_list:
    if user == str(member)[:-5] or user==member.display_name:
      return member
  return False

def check_account(id, data):
  for x in data:
    if str(id) == x:
      return x
  return False 

async def doggy(ctx,bot):
  await ctx.send("https://www.youtube.com/watch?v=Uz9k6QGqXj0")

async def ak47(ctx,bot):
  lan=language(ctx.guild.id)
  currency_data=take_data()
  await ctx.send("你要搶誰?")
  
  def check(m):
    return m.author==ctx.author and m.channel==ctx.channel
  
  try:
    msg=await bot.wait_for(event="message", check=check, timeout=30)
  except asyncio.TimeoutError:
    await ctx.send("等待逾時")
    currency_data[str(ctx.author.id)]["inventory"]["AK47"]+=1
    await rewrite_data(currency_data)
    return
  else:
    pass
  0
  now_time=datetime.datetime.now()
  fine=400
  thirty_minutes=datetime.timedelta(
    minutes=10
  )

  have_member=search_user_in_guild(msg.content, ctx.guild.members)
  if have_member != False:
    have_account2=check_account(have_member.id,currency_data)
    if have_account2 != False:
      for x in currency_data[str(ctx.author.id)]:
        if x=="jail":
          if currency_data[str(ctx.author.id)]["jail"]!=False:
            last_time=datetime.datetime.fromtimestamp(currency_data[str(ctx.author.id)]["jail"])
            been=now_time-last_time
            if been<=thirty_minutes:
              await ctx.send(lan["currency"]["34"])
              currency_data[str(ctx.author.id)]["inventory"]["AK47"]+=1
              await rewrite_data(currency_data)
              return

      member2_name=have_member.display_name
      
      chance=random.uniform(1,10)
      randomF=random.uniform(300,700)
      get=round(randomF)
      if currency_data[have_account2]["money"] < 0:
        currency_data[have_account2]["money"]=0
      else:  
        currency_data[have_account2]["money"]-=get
      currency_data[str(ctx.author.id)]["money"]+=get
      await ctx.send(lan["currency"]["16"]+member2_name+lan["currency"]["17"]+str(get)+lan["currency"]["4"])
      await rewrite_data(currency_data)
      return
    else:
      await ctx.send(lan["currency"]["19"])
      currency_data[str(ctx.author.id)]["inventory"]["AK47"]+=1
      await rewrite_data(currency_data)
      return
  else:
    await ctx.send(lan["currency"]["15"])
    print(currency_data[str(ctx.author.id)]["inventory"]["AK47"])
    currency_data[str(ctx.author.id)]["inventory"]["AK47"]+=1
    print(currency_data[str(ctx.author.id)]["inventory"]["AK47"])
    await rewrite_data(currency_data)
    return

  