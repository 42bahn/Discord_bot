async def ft_mic_check(ctx, *target):
    if target is None:
        await ctx.reply("모두 음성채널로 들어와주시기 바랍니다. @everyone")
    else:
        # await ctx.send(f"{target}씨! 음성채널로 들어오십시오.")
        await ctx.reply('{target}{}씨!\n 음성채널로 들어오십시오.'.format(', '.join(target)))