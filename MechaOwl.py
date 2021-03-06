import os
import disnake
from disnake.ext import commands


token = os.environ['MECHAOWL_TOKEN']
guild_id = os.environ['MECHAOWL_GUILDID']
bot = commands.InteractionBot(test_guilds=[int(guild_id)])


@bot.event
async def on_ready():
    print('Ready!')


bot.load_extension("cogs.hello")
bot.load_extension("cogs.poll")
bot.load_extension("cogs.quote")
bot.load_extension("cogs.role")
bot.load_extension("cogs.memefy")
bot.load_extension("cogs.pomodoro")


bot.run(token)
