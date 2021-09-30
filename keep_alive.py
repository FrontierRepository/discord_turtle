from flask import Flask, render_template, request
from threading import Thread
import discord
from discord.ext import commands
import main
import asyncio

available_pswd=("haha")

app = Flask('')

@app.route('/')
def home():
  return render_template("update_log.html")

@app.route('/sended')
def sended():
  text=request.args.get("text",default="",type=str)
  idd=request.args.get("channel",default="",type=str)
  password=request.args.get("pswd",default="",type=str)
  if password not in available_pswd:
    return "wrong password"
  channel=bot.get_channel(int(idd))
  asyncio.ensure_future(asyncio.Task(channel.send(text), loop=bot.loop),loop=bot.loop)
  return f"send message to {channel.name}"
  

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive(b:commands.Bot):
  global bot
  bot=b
  server = Thread(target=run)
  server.start()