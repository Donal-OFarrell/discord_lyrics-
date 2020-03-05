'''
Lyrics Discord bot 
API documentation : https://discordpy.readthedocs.io/en/latest/api.html
Donal O' Farrell 
Thanks to https://github.com/iannase/musixmatch-python-api/blob/master/lyrics.py for the breakdown on how to query the musixmatch API
A simple Discord bot intended for private usage which will return 30% of lyrics for a song if the name of the artist and the songname is given in format:
"!lyrics thin lizzy | whiskey in the jar "
No copyright infringement intended 
The musixmatch api is legal to use non-commercially
'''

import random
from random import choice
import os 
from dotenv import load_dotenv # required to load env credentials 
from discord.ext import commands # bot commands from discord.py 
from lyric_api import ping_musix

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # these can be loaded with an associated .env file which contains your credntials, token is unique to you
GUILD = os.getenv('DISCORD_GUILD') # for your server 

bot = commands.Bot(command_prefix='!') # each command to the bot needs to be prefixed with '!'

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to the server.') # onload indication that bot has connected 


@bot.command(name='lyrics',help='returns the lyrics to a song. Enter the artist name followed by | and then the song name. \nFor example "john lennon | imagine"') # command is lyrics

async def lyrics(ctx, *args): # ctx or context is required - see API documentation 
    full_string=''
    song_name=''
    artist=''
    for arg in args:
        full_string += arg + ' ' # pass all args to a single string
    
    ll=full_string.split('|') # delimit by the pipe '|' symbol
    
    artist = ll[0].rstrip() # list index 1 is equal to the artist
    song_name= ll[1].strip() # list index 2 is equal to the songname 
    data = ping_musix(artist,song_name) # call the function 

    await ctx.send("Searching for lyrics for " + song_name.title() + " by " + artist.title() + ".") # search message outputted to discord

    if data == 'error': # if error i.e. song not found or url does not exist 
        not_found = ("I couldn't find lyrics for " + artist + " " + song_name + ", please check your spelling and try again.") # return error 
        await ctx.send(not_found)
    else:
        await ctx.send(data) # otherwise pipe out the lyrics to the discord chat  

bot.run(TOKEN) # credentials 