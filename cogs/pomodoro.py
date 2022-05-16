import disnake
from disnake.ext import commands
from utils.converters import str2sec
import asyncio


class PomodoroCommand(commands.Cog):
    """Manage pomodoro timers."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.thumbnail_url = "https://c.tenor.com/ogsH7Ailje8AAAAC/cat-funny-cat.gif"

    @commands.slash_command()
    async def pomodoro(
        self,
        inter: disnake.CommandInteraction,
        task: str,
        time: str,
    ):
        """Create pomodoro session.
        Parameters
        ----------
        task: What are you working on?
        time: Length of the pomodoro session
        """
        # seconds = await TimeConverter().convert(inter, time)
        _, seconds = str2sec(time)
        description = f"""
        **New pomodoro session for {inter.author}**
        Task: {task}
        """
        embed = disnake.Embed(description=description)
        embed.set_thumbnail(url=self.thumbnail_url)
        await inter.response.send_message(embed=embed)
        await asyncio.sleep(seconds)
        await inter.followup.send(
            f"{inter.author.mention} your pomodoro session is over! Take a break."
        )


def setup(bot: commands.Bot):
    bot.add_cog(PomodoroCommand(bot))
