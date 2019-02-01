from picamera import PiCamera
import discord
from discord.ext import commands
from asyncio import sleep


#region Definitions
with open('auth.json', 'rb') as f:
    auth = json.load(f)
DISCORD_TOKEN = auth["discord_token"]
#endregion

#region Objects
bot = commands.Bot(command_prefix='!')
pi_camera = PiCamera()
#endregion

#region Discord Events
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="bot.timbobimbo.club | !help"))
    print('------')
    print('DISCORD BOT')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
#endregion

#region Discord Commands
@bot.command(pass_context=True)
async def camera(ctx):
    '''Take a picture with PiCamera'''
	await sleep(0.5)
	await self.bot.delete_message(ctx.message)
	
	image_filename = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.jpg")
	camera.start_preview()
	await sleep(5.0)
	camera.capture(image_filename)
	camera.stop_preview()
	
    await bot.send_file(ctx.message.channel, image_filename)
#endregion

# Start the bot
bot.run(DISCORD_TOKEN)