from cgi import test
import pprint
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import Scrapper
from Scrapper import ScrapperTest
from Api import Api
import random

BOT_NAME = "Borgar_bot"

load_dotenv()
##DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_TOKEN = 'OTczNjEzMjA2ODA5NTA1Nzky.GnUKFf.QKV5J9NZhYieVwvDUG5zPyXHPhYEmQmiEcUiWE'
bot = discord.Client()

#scrapper1 = ScrapperTest()
#dict = scrapper1.navigate()

bot_help_message = """
:: Bot Usage ::
`!mc waifu`                   : surprise
"""

available_commands = ['waifu']

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in.')

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    if msg.content == 'hello':
        await msg.channel.send(f'Hey {msg.author}')
    if msg.content == 'goodbye':
        await msg.channel.send(f'Goodbye {msg.author}')

    if msg.content == '!mc':
        #scrapper1 = ScrapperTest()
        #dict = scrapper1.navigate()
        await msg.channel.send(dict)


    if 'BK' in msg.content:
        print('Keyword found')
        await msg.channel.send(f'https://tenor.com/view/saber-eating-bread-ubw-fate-gif-19103530')

    if msg.content == 'waifu please':
        data = Api()
        dict = data.data()
        nbrAléatoire = random.randint(0,98)
        await msg.channel.send(dict[nbrAléatoire])

@bot.command()
async def mc(ctx, arg):
    if arg == 'waifu':
        ##scrapper1 = Scrapper()
        ##dict = scrapper1.navigate()
        ctx.send(f'test success')
        print('success')
    

bot.run(DISCORD_TOKEN)