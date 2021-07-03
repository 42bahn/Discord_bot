import os
import discord, asyncio
from discord.ext import commands
import random

from discord.flags import alias_flag_value

from module.dice import dice

bot = commands.Bot(command_prefix='.', help_command=None)

commands = ['.help', 'ㅎㅇㅇ', 'ㅎㅇ']

################## 봇 상태메시지 '5초' 간격으로 변경 함수
async def cmd_list(commands):
    await bot.wait_until_ready()
    while not bot.is_closed():
        for c in commands:
            await bot.change_presence(status = discord.Status.online, activity = discord.Streaming(c))
            await asyncio.sleep(5)
################## 봇 상태메시지 '5초' 간격으로 변경 함수 END


################## 봇 상태메시지 설정
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity=discord.Game('.help | 제작 '))
    # await cmd_list(commands)
    print('Running.....')
################## 봇 상태메시지 설정 END

################## .help
@bot.command(name='help')
async def embed(ctx) :
    embed = discord.Embed(title = "Commands prefix is   .",
    description = "현재 실행 가능한 명령어", color = 0xffc0cb)
    embed.add_field(name = "ㅎㅇ", value = "봇이 답장해줄거에요.\n", inline=False)
    embed.add_field(name = "ㅎㅇㅇ", value = "봇이 친절하게 답장해줄거에요.\n", inline=False)
    embed.add_field(name = "김요환", value = "Just Try.\n", inline=False)
    embed.add_field(name = "김태훈", value = "Just Try.\n", inline=False)
    embed.add_field(name = "손나성", value = "Just Try.\n", inline=False)
    embed.add_field(name = "송인철", value = "Just Try.\n", inline=False)
    embed.add_field(name = "임석민", value = "Just Try.\n", inline=False)
    embed.add_field(name="Dev.", value = "[https://github.com/42bahn/Discord_bot](<https://github.com/42bahn/Discord_bot>)", inline=False)
    await ctx.send(embed = embed)
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


################## Member INFO
@bot.command(alias=['감자통모짜', '20시 유산균을 먹자'])
async def 송인철(ctx):
    embed = discord.Embed(title = "송 인철",
    description = "", color = 0x62c1cc)
    embed.add_field(name = "생년월일", value = "1897년 10월 24일", inline = False)
    embed.add_field(name = "직업", value = "Secret Agent", inline = False)
    embed.add_field(name = "취미", value = "애니메이션 감상", inline = False)
    await ctx.send(embed = embed)

@bot.command(alias=['후', '후...'])
async def 손나성(ctx):
    embed = discord.Embed(title = "손 나성",
    description = "", color = 0x62c1cc)
    embed.add_field(name = "생년월일", value = "1997년 식목일", inline = False)
    embed.add_field(name = "직업", value = "알수없음", inline = False)
    embed.add_field(name = "취미", value = "알코올 섭취", inline = False)
    await ctx.send(embed = embed)

@bot.command(alias=['XTEN'])
async def 임석민(ctx):
    embed = discord.Embed(title = "임 석민",
    description = "", color = 0x62c1cc)
    embed.add_field(name = "생년월일", value = "1997년 1월 22일", inline = False)
    embed.add_field(name = "직업", value = "개강을 간절히 기다리는 대학생", inline = False)
    embed.add_field(name = "취미", value = "조별 과제", inline = False)
    await ctx.send(embed = embed)

@bot.command(alias=['EggZegg', 'Eggzegg', 'eggZegg', 'eggzegg'])
async def 김태훈(ctx):
    embed = discord.Embed(title = "김 태훈",
    description = "", color = 0x62c1cc)
    embed.add_field(name = "생년월일", value = "1997년 12월 21일", inline = False)
    embed.add_field(name = "직업", value = "CU 지박령", inline = False)
    embed.add_field(name = "취미", value = "폐기 수집", inline = False)
    await ctx.send(embed = embed)

@bot.command(alias=['요비'])
async def 김요환(ctx):
    embed = discord.Embed(title = "김 요환",
    description = "", color = 0x62c1cc)
    embed.add_field(name = "생년월일", value = "1997년 5월 13일", inline = False)
    embed.add_field(name = "직업", value = "수상한 공부방 긴 생머리 아저씨", inline = False)
    embed.add_field(name = "취미", value = "머리카락 흩날리며 뒤돌아보기", inline = False)
    await ctx.send(embed = embed)
################## Member INFO END



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


################## Dice
@bot.command()
async def call_dice(ctx):
    await dice(ctx)
################## Dice End

################## Cleaner
# @bot.command(alias=['청소'])
# async def cleaner(ctx, amount : int):
#     await ctx.channel.purge(limit=amount)

@bot.command(name="청소", pass_context=True)
async def clear(ctx):
    await ctx.channel.purge(limit=5)
################## Cleaner End
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

# token = open("private_token", "r").readline()

bot.run(os.environ['token'])