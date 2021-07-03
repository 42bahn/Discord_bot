import random

################## Dice
async def dice(ctx):
    randnum = random.randint(1, 6)  # 1이상 6이하 랜덤 숫자를 뽑음
    return await ctx.send(f'🧛‍♂️주사위 결과 : {randnum}')
################## Dice End