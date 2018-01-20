# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import time
# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="", command_prefix="~", pm_help = True)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def info():

	await client.say(" fuck off you think I actually have the time to put some actual work into this bot. HELL NO. I'm going to bed it's 11:38, and I've got school tomarrow. ")

@client.command()
async def kpop():
	await client.say('K-Pop is a sin...')
	time.sleep(2)
	await client.say('You are going to hell')


client.run('NDAzNTg4OTA4Mzc5NjY4NDgx.DULcKg.jrLsEaxAI3jqmL-CtFabTVgFk_k')
