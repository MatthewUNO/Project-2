import discord
from discord.ext import commands, tasks

# Attach bot to Discord server
bot = discord.Client()
token = 'OTcxOTQ1NjM4NjA0NDQzNjU4.YnR46g.cxArEL_BAPjoqXfjVD3fCLtT56A'

# Listen to server activity
@bot.event
async def on_ready():
    # Varriable to track number of active servers
    guild_count = 0

    # Loops through affiliated servers
    for guild in bot.guilds:
        # Output server name and ID number
        print(f'- {guild.id} (name: {guild.name})')
        # Increase server count
        guild_count = guild_count + 1
    print('PythonBot is in ' + str(guild_count) + ' guild.')

# Listen for server messages that contain the pre-defined string.
@bot.event
async def on_message(message):
    if message.content == 'Hello':
        await message.channel.send('Hey Buddy!')

bot.run(token)
