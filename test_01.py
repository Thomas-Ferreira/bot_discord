
import discord
import os
from dotenv import load_dotenv

BOT_NAME = "MinecraftBot"

load_dotenv()
##DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_TOKEN = 'OTczNjEzMjA2ODA5NTA1Nzky.GnUKFf.QKV5J9NZhYieVwvDUG5zPyXHPhYEmQmiEcUiWE'
bot = discord.Client()
list_Sortie = []

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'on ma':
        await message.channel.send(f'Hey {message.author}')
    if message.content == 'goodbye':
        await message.channel.send(f'Goodbye {message.author}')

@bot.event
async def on_message(msg):
    if 'BK' in msg.content:
        print('Keyword found')
        await msg.channel.send(f'https://tenor.com/view/saber-eating-bread-ubw-fate-gif-19103530')
    

bot.run(DISCORD_TOKEN)