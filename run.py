import discord
from discord.ext import commands
import json

##### Setup #####
BOT_TOKEN = 'YOUR_TOKEN'
bot = commands.Bot(command_prefix='!', description='Description')
data = None

##### Functions #####
# Load data
def loadData():
	with open('data.txt') as fp:
		data = json.load(fp)

# Save data
def saveData():
	with open('data.txt', 'w') as fp:
		json.dump(data, fp)

##### Discord commands #####
@bot.event
async def on_ready():
	loadData()
	print(bot.user.name + ' is ready!')

@bot.event
async def on_message(message):
	await bot.process_commands(message)

@bot.command(name='hello', description='Test command.')
# Say hello
async def hello():
	await bot.say("Hello!")

@bot.command(name='commandWithArgs', description='Command with args')
# Description of command goes here
async def commandWithArgs(*args):
	await bot.say("CommandWithArgs: ")
	for c in args:
		await bot.say(c + " ")

# Bot Token
bot.run(BOT_TOKEN)
