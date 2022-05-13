import disnake
from disnake.ext import commands


def str2sec(argument: str) -> tuple[str, int]:
    """Handle conversion of time strings like '4m' or '2h' to number of seconds."""
    multipliers = {'s': 1, 'm': 60, 'h': 3600}
    if argument.isdecimal():
        return (f"{argument}m", int(argument) * multipliers['m'])
    amount = argument[:-1]
    units = argument[-1]
    if units in multipliers and amount.isdecimal():
        seconds = int(float(amount) * multipliers[units])
        return (argument, seconds)
    raise commands.errors.BadArgument(message="Invalid time string.")
