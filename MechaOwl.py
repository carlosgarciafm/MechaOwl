import os
from disnake.ext import commands


token = os.environ['MECHAOWL_TOKEN']
guild_id = os.environ['MECHAOWL_GUILDID']
bot = commands.InteractionBot(test_guilds=[int(guild_id)])


@bot.event
async def on_ready():
    print('Ready!')


@bot.slash_command()
async def hello(ctx):
    """Say hello to the user."""
    await ctx.response.send_message(f"Hello {ctx.author.name}!")


bot.run(token)
