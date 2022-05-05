import os
import disnake
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


@bot.slash_command()
async def poll(interaction: disnake.CommandInteraction):
    pass


@poll.sub_command()
async def yesno(
        interaction: disnake.CommandInteraction,
        poll: str,
        title: str | None = None,
        ):
    """Create a pretty yes/no poll.
    Parameters
    ---------------
    poll: what should be the poll be about?
    title: optional title for the poll
    """
    default_emj = [
            '\N{REGIONAL INDICATOR SYMBOL LETTER Y}',
            '\N{REGIONAL INDICATOR SYMBOL LETTER N}',
            ]
    description = f"**{poll}**\n{default_emj[0]}: yes\n{default_emj[1]}: no"
    embed = disnake.Embed(
            title=title or f"New poll by {interaction.author.name}",
            description=description
            )
    msg = await interaction.channel.send(embed=embed)
    for emj in default_emj:
        await msg.add_reaction(emj)


# TODO: force `emj` arguments to be emojis or convert them afterwards to be able
# to add reactions to the embed.
@poll.sub_command()
async def multi(
        interaction: disnake.CommandInteraction,
        poll: str,
        title: str = "",
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
    poll: what should be the poll be about?
    title: optional title for the poll
    opt0: possible answer for the poll
    opt1: possible answer for the poll
    opt2: possible answer for the poll
    opt3: possible answer for the poll
    opt4: possible answer for the poll
    opt5: possible answer for the poll
    opt6: possible answer for the poll
    opt7: possible answer for the poll
    opt8: possible answer for the poll
    opt9: possible answer for the poll
    emj0: reaction for opt0 in the poll
    emj1: reaction for opt1 in the poll
    emj2: reaction for opt2 in the poll
    emj3: reaction for opt3 in the poll
    emj4: reaction for opt4 in the poll
    emj5: reaction for opt5 in the poll
    emj6: reaction for opt6 in the poll
    emj7: reaction for opt7 in the poll
    emj8: reaction for opt8 in the poll
    emj9: reaction for opt9 in the poll
    """
    default_emj = [

            '\N{REGIONAL INDICATOR SYMBOL LETTER A}',
            '\N{REGIONAL INDICATOR SYMBOL LETTER B}',
            '\N{REGIONAL INDICATOR SYMBOL LETTER C}',
            '\N{REGIONAL INDICATOR SYMBOL LETTER D}',
            '\N{REGIONAL INDICATOR SYMBOL LETTER E}',
            '\N{REGIONAL INDICATOR SYMBOL LETTER F}',
            '\N{REGIONAL INDICATOR SYMBOL LETTER G}',
            '\N{REGIONAL INDICATOR SYMBOL LETTER H}',
            '\N{REGIONAL INDICATOR SYMBOL LETTER I}',
            '\N{REGIONAL INDICATOR SYMBOL LETTER J}',
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
    embed = disnake.Embed(title=title or f"New poll by {interaction.author.name}", description=description)
    msg = await interaction.channel.send(embed=embed)
    for emj in emjs:
        await msg.add_reaction(emj)


bot.run(token)
