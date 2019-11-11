import discord
import json
from discord.ext import commands
from asyncio import sleep

from auth import DISCORD_TOKEN

#region Objects
bot = commands.Bot(command_prefix='$')
#endregion

#region Discord Events
@bot.event
async def on_ready():
    '''
    presence = discord.Streaming(
        name="Dying", 
        url="github.timbobimbo.club", 
        details="$help",
        assets={
            "large_image": "hero",
            "large_text": "hero",
            "small_image": "hero",
            "small_text": "hero"
        }
    )
    
    await bot.change_presence()
    '''
    print('------')
    print('DISCORD BOT')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
#endregion

#region Discord Commands
@bot.command(pass_context=True)
async def fetch(ctx, limit, channel_id=None):
    '''Fetch message from channel'''
    await sleep(0.5)
    await ctx.message.delete()

    limit_num = 0
    try:
        limit_num = int(limit)
    except:
        limit_num = 1
    
    if limit is 0:
        limit = None
    
    if channel_id is not None:
        channel = bot.get_channel(channel_id)
    else:
        channel = ctx.message.channel
    
    messages = []
    async for message in channel.history(limit=limit_num):
        messages.append(message.content)
    
    with open("ex.json", "wb") as f:
        json.dump(f, messages, indent=4)
        
    async with channel.typing():
        await channel.send("bra!")
#endregion

# Start the bot
bot.run(DISCORD_TOKEN)
