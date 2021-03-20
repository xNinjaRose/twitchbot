import os
from twitchio.ext import commands
import requests 
import urlfetch 

bot = commands.Bot(
    #Set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

#bot.py, below bot object
@bot.event 
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws=bot._ws #this is only needed to send messages within eventy ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has arrived!!!")

@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat'

    #make sure the bot ignores itself and streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return 
    #await ctx.channel.send(ctx.content) DO NOT UNCOMMENT UNLESS YOU WANT TO BE ANNOYED
    await bot.handle_commands(ctx)

#bot.py, below event message function
@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!!')

@bot.command(name='diablo3')
async def diablo3(ctx):
    await ctx.send('The results so far of the Diablo 1 Life are https://bit.ly/3cQpThk !')

@bot.command(name='followage')
async def followage(ctx):
    username = ctx.author.name
    follow = urlfetch.get(f"https://api.2g.be/twitch/followage/{os.environ['CHANNEL']}/{username}")
    await ctx.send((follow.content.decode('UTF-8'))) 

@bot.command(name='rules')
async def rules(ctx):
    await ctx.send('''The rules I play Bl2 by are: No Farming, No BA Ranks, No gold keys, Must keep mission level normal or higher,
    Class Mod Mis-match Exception''')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hey @{ctx.author.name}!!')

@bot.command(name='advice')
async def advice(ctx):
    await ctx.send(f'Please refrain from giving any sort of advice about the game, or how to play the game. @{ctx.author.name}')

#bot.py
if __name__ == "__main__":
    bot.run()
