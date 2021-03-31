# --------------------------------------------------------------------------------
# first, find "MEMO:" comment.
# rewrite it for yourself.
# --------------------------------------------------------------------------------

import discord
from discord.ext import commands

# MEMO: bot token
TOKEN = "BOT_TOKEN"

# MEMO: muter channel id
muter_channel_id = 00000000000000000

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Login check')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_voice_state_update(member, before, after):
    global muter_channel_id
    print('on_voice_state_update')
    if before.channel != after.channel:
        if after.channel != None and after.channel.id == muter_channel_id:
            await member.edit(mute=True)

        if before.channel != None and before.channel.id == muter_channel_id:
            await member.edit(mute=False)

client.run(TOKEN)