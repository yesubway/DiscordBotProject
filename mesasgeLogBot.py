# writen by yesubway
# when 2023. 05. 23.
# DiscordBotproject
# messageLogBot.py

import datetime
import discord
from discord.ext import commands
import enc
TOKEN_KEY = enc.SERVER_SECRET_KEYS

# Authorization Setting (discord.py 1.7.3.)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
# bot = commands.Bot(command_prefix='!', intents=intents)

# Authorization Setting (discord.py 2.0.)
#intents.messages = True
#intents.message_content = True
#intents.guild_messages = True
#intents.dm_messages = True

# Intents Setting Other
# client = discord.Client(intents=intents)
# client = discord.Client()
# client = discord.Client(discord.Intents.default())
# client = discord.Client(discord.Intents.all())

@bot.event
async def on_ready() :
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Test Bot Started !'))
    print('[messageLogBot start complete!]')

@bot.event
async def on_message(msg) :
    # Log Write Start
    with open("message.log", "a", encoding="utf-8") as messageLogFile:
        log = f"{msg.created_at} {msg.guild} {msg.channel} {msg.author} {msg.content}"
        print(log)
        messageLogFile.write(log+"\n")

        # Bot Message Ignore
        if msg.author == bot.user or msg.author.bot:
            return

        if msg.content.startswith("!"):
            msgparam = msg.content[1:].split()

            if msgparam[0] == "안녕":
                await msg.channel.send("안녕하세요!")

            if msgparam[0] == "시간":
                nowhhmm = datetime.datetime.now()
                await msg.channel.send(f"지금 시간은 {nowhhmm.hour}시 {nowhhmm.minute}분 입니다.")

            if msgparam[0] == "날짜":
                nowyyyymmdd = datetime.datetime.now()
                await msg.channel.send(f"오늘은 {nowyyyymmdd.year}년 {nowyyyymmdd.month}월 {nowyyyymmdd.day}일 입니다.")

    return

bot.run(TOKEN_KEY)