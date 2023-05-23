# writen by yesubway
# when 2022. 06. 13.
# DiscordBotproject
# informationBot.py

# update 2023.05.23.
# 1 TOKEN 새로 발급, github upload를 위해 ignoreFile에 저장
# 2 서버에서 명령어 실행X 현상.. DM에선 실행O..
# 3 serverBot을 새로 생성함..
# 4 discord.py 1.7.3 install..
# comment end

import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')

import enc
TOKEN_KEY = enc.INFO_SECRET_KEYS

# on_ready : 봇이 준비 완료 상태면 호출되는 함수 .
@bot.event
async def on_ready() :
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Halo !'))
    print('[informationBot start complete!]')

# on_message : 명령어 실행 / bot의 메세지는 무시
@bot.event
async def on_message(msg) :
    if msg.author.bot : return None
    await bot.process_commands(msg)

# 소개
@bot.command()
async def 소개(ctx) :
    embed = discord.Embed(title='명령어 안내', description='fresh_robot의 명령어 모음입니다.'
                          , colour=0xff7676)
    embed.add_field(name='인사', value='안녕\r\nhi')
    embed.add_field(name='삭제', value='삭제\r\ndelete')
    embed.add_field(name='공지사항', value='공지사항\r\nnotice')
    embed.add_field(name='공지올리기', value='공지등록\r\naddNoti')
    embed.add_field(name='공지내리기', value='공지삭제\r\ndelNoti')
    embed.set_footer(text='더 다양한 명령어를 준비 중 입니다.')
    await ctx.channel.send(embed=embed)

# 인사
@bot.command()
async def 안녕(ctx) :
    await ctx.channel.send('Hi!')

@bot.command()
async def hi(ctx) :
    await ctx.channel.send('Hi!')

# 삭제 : 최근 입력된 메세지 2개 삭제(삭제메세지 & 이전메세지)
@bot.command()
async def 삭제(ctx) :
    await ctx.channel.purge(limit=2)

@bot.command()
async def delete(ctx) :
    await ctx.channel.purge(limit=2)

# 고정 리턴
# 이건 실행 안된다.
# https://stackoverflow.com/questions/68219913/discord-py-message-pinning
# @bot.command()
# async def pin1(ctx, message_id: int) :
#    message = await ctx.fetch_message(message_id)
#    await message.pin()

# 고정 리턴
# @bot.command()
# async def 고정(ctx) :
#    await ctx.message.pin()

# 반드시 토큰 값 셋팅 필수, 토큰이 없으면 실행되지 않는다.
bot.run(TOKEN_KEY)