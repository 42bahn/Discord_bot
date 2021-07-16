import discord

async def manual(ctx) :
    embed = discord.Embed(title = "Commands prefix is   .",
    description = "현재 실행 가능한 명령어\n---------------------------------", color = 0xffc0cb)
    embed.add_field(name = "서버명", value = "현재 서버의 이름을 알려줍니다.\n", inline=False)
    embed.add_field(name = "나(me)", value = "나의 디스코드 ID를 알려줍니다.\n", inline=False)
    embed.add_field(name = "ㅎㅇ", value = "봇이 답장해줄거에요.\n", inline=False)
    embed.add_field(name = "ㅎㅇㅇ", value = "봇이 친절하게 답장해줄거에요.\n", inline=False)
    embed.add_field(name = "Member RealName or Nickname", value = "Just Try.\n", inline=False)
    embed.add_field(name = "날씨", value = "봇이 날씨 정보를 알려줍니다.\n", inline=False)
    

    embed.add_field(name="Dev.", value = "[https://github.com/42bahn/Discord_bot](<https://github.com/42bahn/Discord_bot>)", inline=False)
    await ctx.reply(embed = embed)