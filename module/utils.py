import discord, asyncio

################## 봇 상태메시지 '5초' 간격으로 변경 함수 (commands : 배열)
## commands = ['.help', 'ㅎㅇㅇ', 'ㅎㅇ']
async def cmd_list(bot, commands):
    await bot.wait_until_ready()
    while not bot.is_closed():
        for c in commands:
            await bot.change_presence(status = discord.Status.online, activity = discord.Streaming(c))
            await asyncio.sleep(5)
################## 봇 상태메시지 '5초' 간격으로 변경 함수 END