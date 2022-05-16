import disnake
from disnake.ext import commands


class PollCommand(commands.Cog):
    """Create a pretty poll."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def bpoll(
        self,
        inter: disnake.CommandInteraction,
        poll: str,
        title: str | None = None,
    ):
        """Create a pretty yes/no poll.
        Parameters
        ---------------
        poll: What should be the poll be about?
        title: Title for the poll
        """
        default_emj = [
            "\N{REGIONAL INDICATOR SYMBOL LETTER Y}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER N}",
        ]
        description = f"**{poll}**\n{default_emj[0]}: yes\n{default_emj[1]}: no"
        embed = disnake.Embed(
            title=title or f"New poll by {inter.author.name}", description=description
        )
        # Hackish way to prevent "bot is thinking" or "command failed" messages.
        await inter.response.defer()
        msg = await inter.channel.send(embed=embed)
        for emj in default_emj:
            await msg.add_reaction(emj)
        if inter.response._responded:
            await inter.delete_original_message()

    @commands.slash_command()
    async def mpoll(
        self,
        inter: disnake.CommandInteraction,
        poll: str,
        title: str | None = None,
        opt0: str | None = None,
        opt1: str | None = None,
        opt2: str | None = None,
        opt3: str | None = None,
        opt4: str | None = None,
        opt5: str | None = None,
        opt6: str | None = None,
        opt7: str | None = None,
        opt8: str | None = None,
        opt9: str | None = None,
        emj0: str | None = None,
        emj1: str | None = None,
        emj2: str | None = None,
        emj3: str | None = None,
        emj4: str | None = None,
        emj5: str | None = None,
        emj6: str | None = None,
        emj7: str | None = None,
        emj8: str | None = None,
        emj9: str | None = None,
    ):
        """Create a pretty poll with multiple options.
        Parameters
        ---------------
        poll: What should be the poll be about?
        title: Title for the poll
        opt0: Possible answer for the poll
        opt1: Possible answer for the poll
        opt2: Possible answer for the poll
        opt3: Possible answer for the poll
        opt4: Possible answer for the poll
        opt5: Possible answer for the poll
        opt6: Possible answer for the poll
        opt7: Possible answer for the poll
        opt8: Possible answer for the poll
        opt9: Possible answer for the poll
        emj0: Reaction for opt0 in the poll
        emj1: Reaction for opt1 in the poll
        emj2: Reaction for opt2 in the poll
        emj3: Reaction for opt3 in the poll
        emj4: Reaction for opt4 in the poll
        emj5: Reaction for opt5 in the poll
        emj6: Reaction for opt6 in the poll
        emj7: Reaction for opt7 in the poll
        emj8: Reaction for opt8 in the poll
        emj9: Reaction for opt9 in the poll
        """
        default_emj = [
            "\N{REGIONAL INDICATOR SYMBOL LETTER A}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER B}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER C}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER D}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER E}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER F}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER G}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER H}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER I}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER J}",
        ]
        options = {
            opt0: emj0 or default_emj[0],
            opt1: emj1 or default_emj[1],
            opt2: emj2 or default_emj[2],
            opt3: emj3 or default_emj[3],
            opt4: emj4 or default_emj[4],
            opt5: emj5 or default_emj[5],
            opt6: emj6 or default_emj[6],
            opt7: emj7 or default_emj[7],
            opt8: emj8 or default_emj[8],
            opt9: emj9 or default_emj[9],
        }
        emjs = [e for o, e in options.items() if o]
        description = f"**{poll}**"
        for opt, emj in options.items():
            if opt:
                description += f"\n{emj}: {opt}"
        embed = disnake.Embed(
            title=title or f"New poll by {inter.author.name}", description=description
        )
        await inter.response.defer()
        msg = await inter.channel.send(embed=embed)
        for emj in emjs:
            await msg.add_reaction(emj)
        if inter.response._responded:
            await inter.delete_original_message()


def setup(bot: commands.Bot):
    bot.add_cog(PollCommand(bot))
