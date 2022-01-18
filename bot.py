from datetime import datetime
import os
import discord, asyncio
from discord import channel
from discord import message
from discord.ext import commands
from discord.flags import alias_flag_value
import sqlite3
import random

from module.dice import dice
from module.member import 송인철, 손나성, 임석민, 김태훈, 김요환, 김규철, 안범준
from module.manual import manual
# from module.weather import naver_weather
from module.clear import ft_clear
from module.mic_check import ft_mic_check as 마쳌
bot = commands.Bot(command_prefix='.', help_command=None)

def member_db_check(id):
    alr_exist = []
    con = sqlite3.connect(r'member.db', isolation_level = None)
    cur = con.cursor()
    cur.execute("SELECT id FROM Member WHERE id = ?", (id,))
    rows = cur.fetchall()
    for i in rows :
        alr_exist.append(i[0])
    if id not in alr_exist :
        return 0
    elif id in alr_exist :
        return 1
    con.close()

@bot.command(aliases=['가입', '등록'])
async def sign_up(ctx):
    con = sqlite3.connect(r'member.db', isolation_level=None)
    cur = con.cursor()
    if member_db_check(ctx.author.id) == 0:
        cur.execute("INSERT INTO Member VALUES(?, ?, ?, ?, ?)", \
            (ctx.author.id, ctx.author.name, 'NULL', 'NULL', datetime.now(),))
    await ctx.send('등록 완료')

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
    await ctx.send(content='어 그래 어서오고. 잘 지내냐?', tts=True)

@bot.command(aliases=['ㅎㅇ', '하이'])
async def hello2(ctx):
    await ctx.send('어 그래')

@bot.command(aliases=['ㅎㅇㄹ', '하이루', '하잉'])
async def hello3(ctx):
    await ctx.send('방가방가')
################## 인사 명령어 EMD

# @bot.command(aliases=['날씨'])
# async def weather(ctx):
#     await naver_weather(ctx)

################## Member INFO
@bot.command(aliases=['송인철', '인철' '감자통모짜', '20시 유산균을 먹자'])
async def call_송인철(ctx):
    await 송인철(ctx)

@bot.command(aliases=['손나성', '후', '후...', '나성'])
async def call_손나성(ctx):
    await 손나성(ctx)

@bot.command(aliases=['임석민', 'XTEN', '석민'])
async def call_임석민(ctx):
    await 임석민(ctx)

@bot.command(aliases=['김태훈', 'EggZegg', 'Eggzegg', 'eggZegg', 'eggzegg'])
async def call_김태훈(ctx):
    await 김태훈(ctx)

@bot.command(aliases=['김요환', '요비', '요환'])
async def call_김요환(ctx):
    await 김요환(ctx)

@bot.command(aliases=['김규철', '규철', '규철이', '규철아', '규스터', '하키미'])
async def call_김규철(ctx):
    await 김규철(ctx)

@bot.command(aliases=['안범준', '앙범', '범준'])
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
    await ctx.send(content=server_name, delete_after=10)

@bot.command(name="나")
async def me(ctx):
    client = ctx.author
    await ctx.send(client, delete_after=10)

@bot.command(aliases=['ㅁㅊ', '맠쳌', '마이크체크', '마쳌', 'ㅁㅊㅁㅊ'])
async def mic_check(ctx, *target):
    await 마쳌(ctx, *target)

@bot.command(aliases=['노래도우미'])
async def 도우미(ctx, *target):
    embed = discord.Embed(title = "노래도우미 사용법",
    description = "", color = 0x62c1cc)
    # embed.set_image(url="sonycast.GIF")
    embed.add_field(name = "!playnow <link/query>", value = "바로 재생", inline = False)
    embed.add_field(name = "!play <link/query>", value = "재생목록 추가", inline = False)
    embed.add_field(name = "!playskip <link/query>", value = "현재 재생곡 스킵하고 입력한 링크 재생", inline = False)
    embed.add_field(name = "!search <query>", value = "유튜브 검색", inline = False)
    embed.add_field(name = "!loop", value = "현재 재생목록 반복", inline = False)
    embed.add_field(name = "!rewind <time>", value = "time 만큼 되감기", inline = False)
    embed.add_field(name = "!forward <time>", value = "time 만큼 앞으로 이동", inline = False)
    embed.add_field(name = "!pause", value = "일시 정지", inline = False)
    embed.add_field(name = "!resume", value = "재개", inline = False)
    embed.add_field(name = "!clear <@user>", value = "모든 재생목록 제거 (또는 특정 유저가 추가한 재생목록 제거", inline = False)
    embed.add_field(name = "!disconnect", value = "노래도우미(Rythm) 연결종료", inline = False)
    embed.add_field(name = "More", value = "[Rythm](<https://rythm.fm/docs/commands/>)")
    await ctx.reply(embed = embed)

# @bot.command(aliases=['추방'])
# async def member_kick(ctx, *target):
#     # member = message.guild.get_member(int(message.content.split(" ")[1]))
#     # await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))
#     await ctx.reply('{}씨!\n 당장 나가주세요.'.format(', '.join(target)))

@bot.command(aliases=['저녁추천', '저녁 추천', '저녁 추천 좀'])
async def member_kick(ctx):
    menu = ['백반', '불백', '치킨', '피자', '자장면', '햄버거', '초밥', '생선구이', '생선조림',
            '다이어트', '돈까스', '덮밥', '분식', '라면', '짜파게티', '스테이크']
    await ctx.reply('{}'.random.shuffle(menu))

@bot.command()
async def 입력하는척(ctx):
    await ctx.trigger_typing()

@bot.command()
async def test(ctx):
    await ctx.trigger_typing()
################## Test End

@bot.command(aliases=['청소'])
async def clear(ctx, number : int=None):
    await ft_clear(ctx, number)

# token = open("private_token", "r").readline()
# bot.run(token)
bot.run(os.environ['token'])
