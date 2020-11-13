import os
import sqlite3
import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix='!')
TOKEN = open("token.txt", "r").read()

db = sqlite3.connect('klaus.db', timeout=10)

@bot.event
async def on_ready():
    print(f'Bot Connected as: {bot.user}')
    await bot.change_presence(activity = discord.Activity(
                              type = discord.ActivityType.watching,
                              name = "Hallmark Christmas Movies"))

@bot.event
async def on_message(message):
    if message.content == 'test':
        await message.channel.send('Testing 1 2 3!')
    
    await bot.process_commands(message)

@bot.command(name='server')
async def fetchServerInfo(context):
    guild = context.guild

    await context.send(f'Server Name: {guild.name}')
    await context.send(f'Server Size: {len(guild.members)}')

@bot.command(name='join')
async def collectUsername(ctx):
    print(ctx.author.display_name)

bot.run(TOKEN)