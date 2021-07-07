async def ft_clear(ctx, number : int=None):
    if ctx.guild:
        print(ctx.guild)
        if ctx.message.author.guild_permissions.manage_messages:
            print(ctx.message.author.guild_permissions.manage_messages)
            # try:
            if number is None:
                print(1)
                await ctx.send('숫자를 입력해주세요')
            elif 50 < number:
                print(2)
                await ctx.message.delete()
                await ctx.send(f'{ctx.message.author.mention} 50보다 큰 수는 입력할 수 없습니다.', delete_after=5)
            else:
                print(3)
                deleted = await ctx.message.channel.purge(limit=number)
                print(3)
                await ctx.send(f'{ctx.message.author.mention}에 의해 {len(deleted)} 개의 메세지가 삭제되었습니다.')
            # except:
            #     await ctx.send("오류")
        else:
            await ctx.send('이 명령을 사용할 수 있는 권한이 없습니다.')
    else:
        await ctx.send('현재 채널에서는 불가능한 명령입니다.')