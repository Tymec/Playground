import discord
import json
from discord.ext import commands
from asyncio import sleep
import datetime

from auth import DISCORD_TOKEN

#region Objects
bot = commands.Bot(command_prefix='$')
#endregion

#region Variables
output_file = "F://Downloads//output.json"
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
async def fetch(ctx, limit, filters=[]):
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

    if filters is not []:
        pass
    
    channel = ctx.message.channel
    
    messages = {}
    iter = 1
    async with channel.typing():
        async for message in channel.history(limit=limit_num):
            message_content = {}
            message_content["author"] = {"id": message.author.id, "name": message.author.name}
            message_content["created_at"] = message.created_at.strftime("%m/%d/%Y, %H:%M:%S")
            message_content["content"] = message.content
            message_content["embeds"] = [str(embed.url) for embed in message.embeds]
            message_content["attachments"] = [attachment.url for attachment in message.attachments]
            message_content["jump_url"] = message.jump_url
            messages[f"Message-{str(iter)}"] = message_content
            print(iter, end="\r")
            iter += 1
    
    with open(output_file, "w") as f:
        json.dump(messages, f, indent=4)
        
    await channel.send("bra!")
#endregion

# Start the bot
bot.run(DISCORD_TOKEN)
