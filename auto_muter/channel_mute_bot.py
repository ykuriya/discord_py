# --------------------------------------------------------------------------------
# first, find "MEMO:" comment.
# rewrite it for yourself.
# --------------------------------------------------------------------------------

import discord
from discord.ext import commands

# MEMO: bot token
TOKEN = "BOT_TOKEN"

# MEMO: muter channel id
mute_channel_ids = [00000000000000000]

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Login check')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_voice_state_update(member, before, after):
    global mute_channel_ids

    # --------------------------------------------------------------------------------
    # voice state cannot edit after being "disconnect" voice channel.
    # voice state unmute when "connect".
    # --------------------------------------------------------------------------------

    # on_disconnect
    if member.voice == None:
        return

    # mute:     when connect to mute channels.
    # unmute:   when "new connect" or connect to other channels.
    if before.channel != after.channel:
        if after.channel != None and after.channel.id in mute_channel_ids:
            await member.edit(mute=True)
        elif before.channel == None or before.channel.id in mute_channel_ids:
            await member.edit(mute=False)

client.run(TOKEN)
