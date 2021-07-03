import discord

async def 송인철(ctx):
    embed = discord.Embed(title = "송 인철",
    description = "", color = 0x62c1cc)
    embed.add_field(name = "생년월일", value = "1897년 10월 24일", inline = False)
    embed.add_field(name = "직업", value = "Secret Agent", inline = False)
    embed.add_field(name = "취미", value = "애니메이션 감상", inline = False)
    await ctx.send(embed = embed)