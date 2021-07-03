import discord

async def manual(ctx) :
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