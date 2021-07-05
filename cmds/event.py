import discord
from discord.ext import commands
from core.classes import cog_extension

class event(cog_extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(860469237214740491)
        await channel.send(">>"+str(member)+" join!")
    #在成員加入時發送訊息
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(860469237214740491)
        await channel.send(">>"+str(member)+" leave!")
    #在成員離開時發送訊息

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg == "you know the rules":
            await msg.channel.send("and so do I")
    #在偵測到特定訊息時回復

def setup(bot):
    bot.add_cog(event(bot))