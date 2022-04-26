import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
token = os.environ['MECHAOWL_TOKEN']


@bot.event
async def on_ready():
    print('Ready!')


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")


bot.run(token)
