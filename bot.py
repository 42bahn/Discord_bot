import os
import discord, asyncio
from discord import channel
from discord.ext import commands
import random

from discord.flags import alias_flag_value

from module.dice import dice
from module.member import 송인철, 손나성, 임석민, 김태훈, 김요환, 안범준
from module.manual import manual
from module.weather import naver_weather
bot = commands.Bot(command_prefix='.', help_command=None)

################## 봇 상태메시지 설정
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.dnd, activity=discord.Game('.help | 제작 '))
    # await cmd_list(commands)
    print('Running.....')
################## 봇 상태메시지 설정 END

################## Welcome & GoodBye Message
@bot.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님'
    channel = member.server.get_channel("channel_id_here")
    await bot.send_message(channel, fmt.format(member, member.server))
 
@bot.event
async def on_member_remove(member):
    channel = member.server.get_channel("channel_id_here")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await bot.send_message(channel, fmt.format(member, member.server))
################## Welcome & GoodBye Message End

################## .help
@bot.command(aliases=['도움'])
async def help(ctx) :
    await manual(ctx)
################## .help EMD


################## 인사 명령어
@bot.command(aliases=['ㅎㅇㅇ', '하이염', '하이여'])
async def hello1(ctx):
    await ctx.send('어 그래 어서오고. 잘 지내냐?')

@bot.command(aliases=['ㅎㅇ', '하이'])
async def hello2(ctx):
    await ctx.send('어 그래')

@bot.command(aliases=['ㅎㅇㄹ', '하이루', '하잉'])
async def hello3(ctx):
    await ctx.send('방가방가')
################## 인사 명령어 EMD

@bot.command(aliases=['날씨'])
async def weather(ctx):
    await naver_weather(ctx)

################## Member INFO
@bot.command(aliases=['송인철', '감자통모짜', '20시 유산균을 먹자'])
async def call_송인철(ctx):
    await 송인철(ctx)

@bot.command(aliases=['손나성', '후', '후...'])
async def call_손나성(ctx):
    await 손나성(ctx)

@bot.command(aliases=['임석민', 'XTEN'])
async def call_임석민(ctx):
    await 임석민(ctx)

@bot.command(aliases=['김태훈', 'EggZegg', 'Eggzegg', 'eggZegg', 'eggzegg'])
async def call_김태훈(ctx):
    await 김태훈(ctx)

@bot.command(aliases=['김요환', '요비'])
async def call_김요환(ctx):
    await 김요환(ctx)

@bot.command(aliases=['안범준', '앙범'])
async def call_안범준(ctx):
    await 안범준(ctx)
################## Member INFO END

################## Dice
@bot.command(aliases=['dice'])
async def call_dice(ctx):
    await dice(ctx)
################## Dice End

################## Test
@bot.command(name="서버명")
async def server_name(ctx):
    server_name = ctx.guild
    await ctx.send(server_name)

@bot.command(name="나")
async def me(ctx):
    client = ctx.author
    await ctx.send(client)

################## Test End
#
# @bot.event
# async def on_message(message):
#     if message.content.startswith('.game'):
#         embed = discord.Embed(title="설문조사", description="설문조사", color=0x00aaaa)
#         embed.add_field(name="⭕️", value="ㄹㅇ")
#         embed.add_field(name="❌", value="ㄴㄴ")
#         msg = await message.channel.send(embed=embed)
#         await msg.add_reaction("⭕️") #step
#         await msg.add_reaction("❌") #stun

# @bot.event
# async def on_reaction_add(reaction, user):
#     if user.bot == 1: #봇이면 패스
#         return None
#     if str(reaction.emoji) == "🦶":
#         await reaction.message.channel.send(user.name + "님이 step 아이템을 구매")
#     if str(reaction.emoji) == "⚔️":

#         await reaction.message.channel.send(user.name + "님이 stun 아이템을 구매")

token = open("private_token", "r").readline()
bot.run(token)
# bot.run(os.environ['token'])
