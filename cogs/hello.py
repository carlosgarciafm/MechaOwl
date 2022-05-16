import disnake
from disnake.ext import commands


class HelloCommand(commands.Cog):
    """Say hello to the user."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def hello(self, inter: disnake.CommandInteraction):
        """Say hello to the user."""
        await inter.response.send_message(f"Hello {inter.author.name}!")


def setup(bot: commands.Bot):
    bot.add_cog(HelloCommand(bot))
