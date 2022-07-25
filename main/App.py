from cgi import test
import discord
from discord.ext import commands
from dotenv import load_dotenv
from Data.Api import Api
from Data.EpicGamesApi import EpicGamesApi
import random

BOT_NAME = "Borgar_bot"

load_dotenv()
##DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_TOKEN = 'OTczNjEzMjA2ODA5NTA1Nzky.GnUKFf.QKV5J9NZhYieVwvDUG5zPyXHPhYEmQmiEcUiWE'
bot = discord.Client()

bot_help_message = """
:: Bot Usage ::
`$borgar`                   : show help
`$test`                     : test command
`$borgar waifu`             : surprise
`$waifu`                    : surprise
"""

bot = commands.Bot(command_prefix='$')

def getResultApi(arg) :
    data = Api()
    dict = data.dataPybooru(arg)
    return dict

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

    if msg.content == '$borgar':
        await msg.channel.send(bot_help_message)

    if 'BK' in msg.content:
        print('Keyword found')
        await msg.channel.send(f'https://tenor.com/view/saber-eating-bread-ubw-fate-gif-19103530')

    if msg.content == 'waifu please':
        data = Api()
        dict = data.data()
        nbrAléatoire = random.randint(0,99)
        await msg.channel.send(dict[nbrAléatoire])

    await bot.process_commands(msg)

@bot.command()
async def borgar(ctx, arg):
    if arg == 'help':
        await ctx.send(bot_help_message)

    if arg == 'waifu':
        data = Api()
        dict = data.dataPybooru()
        nbrAléatoire = random.randint(0,99)
        await ctx.channel.send(dict[nbrAléatoire])
        print('success')
    
@bot.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

@bot.command()
async def waifu(ctx, arg):
    dict = getResultApi(arg)
    nbrAléatoire = random.randint(0,99)
    print(dict[nbrAléatoire])
    await ctx.channel.send(dict[nbrAléatoire])
    #await ctx.channel.send('error : {0}'.format(TypeError))
    print('success')

@bot.command()
async def freeGames(ctx, arg):
    data = EpicGamesApi()
    dict = data.getFreeGames()
    await ctx.channel.send(dict)
    print('sucess')


bot.run(DISCORD_TOKEN)