import discord, asyncio
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='.', help_command=None)

commands = ['.help', 'ㅎㅇㅇ', 'ㅎㅇ']

# 봇 상태메시지 '5초' 간격으로 변경
async def cmd_list(commands):
    await bot.wait_until_ready()
    while not bot.is_closed():
        for c in commands:
            await bot.change_presence(status = discord.Status.online, activity = discord.Streaming(c))
            await asyncio.sleep(5)

@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity=discord.Game('.help | 제작 '))
    # await cmd_list(commands)
    print('Set [State Massage]')

@bot.command(aliases=['ㅎㅇㅇ', '하이염', '하이여'])
async def hello1(ctx):
    await ctx.send('어 그래 어서오고. 잘 지내냐?')

@bot.command(aliases=['ㅎㅇ', '하이'])
async def hello2(ctx):
    await ctx.send('어 그래')

@bot.command(aliases=['ㅎㅇㄹ', '하이루', '하잉'])
async def hello3(ctx):
    await ctx.send('방가방가')

@bot.command()
async def 송인철(ctx):
    embed = discord.Embed(title = "송 인철",
    description = "", color = 0x62c1cc)
    embed.add_field(name = "생년월일", value = "1897년 10월 24일", inline = False)
    embed.add_field(name = "직업", value = "Secret Agent", inline = False)
    embed.add_field(name = "취미", value = "애니메이션 감상", inline = False)
    await ctx.send(embed = embed)

@bot.command()
async def 손나성(ctx):
    embed = discord.Embed(title = "손 나성",
    description = "", color = 0x62c1cc)
    embed.add_field(name = "생년월일", value = "1997년 식목일", inline = False)
    embed.add_field(name = "직업", value = "알수없음", inline = False)
    embed.add_field(name = "취미", value = "알코올 섭취", inline = False)
    await ctx.send(embed = embed)

@bot.command(name='help')
async def embed(ctx) :
    embed = discord.Embed(title = "Commands prefix is   .",
    description = "현재 실행 가능한 명령어", color = 0xffc0cb)
    embed.add_field(name = "ㅎㅇ", value = "봇이 답장해줄거에요.\n", inline=False)
    embed.add_field(name = "ㅎㅇㅇ", value = "봇이 친절하게 답장해줄거에요.\n", inline=False)
    embed.add_field(name = "송인철", value = "Just Try.\n", inline=False)
    embed.set_footer(text = "다양한 의견 제시 바람")
    await ctx.send(embed = embed)

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