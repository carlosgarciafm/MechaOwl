import disnake
from disnake.ext import commands
from urllib import request
from json import loads


memes = dict()
try:
    response = request.Request(
        "https://api.memegen.link/templates/", headers={"User-Agent": "Mozilla/5.0"}
    )
    meme_list = loads(request.urlopen(response).read())
    memes = {
        meme["name"]: {"id": meme["id"], "lines": meme["lines"]} for meme in meme_list
    }
except:
    print("meme list could not be loaded")


def escape(string: str) -> str:
    """Escape special characters."""
    for old, new in [
        ("-", "--"),
        (" ", "-"),
        ("_", "__"),
        ("?", "~q"),
        ("%", "~p"),
        ("#", "~h"),
        ("/", "~s"),
        ('"', "''"),
    ]:
        string = string.replace(old, new)
    return string


class MemefyCommand(commands.Cog):
    """Create a meme using [memegen](jacebrowning/memegen)."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.apiurl = "https://api.memegen.link"
        self.memes = memes

    @commands.slash_command()
    async def meme(
        self,
        inter: disnake.CommandInteraction,
        name: str,
        top: str,
        bottom: str,
        gif: bool = False,
    ):
        """Send a meme to spec.
        Parameters
        -----------
        name: Name of the meme
        top: Top text
        bottom: Bottom text
        gif: Do you want a gif?
        """
        req_url = (
            f"{self.apiurl}/{self.memes[name]['id']}/{escape(top)}/{escape(bottom)}"
        )
        req_url += gif and ".gif" or ".png"

        await inter.response.defer()
        embed = disnake.Embed()
        embed.set_footer(text="Powered by memegen API.")
        embed.set_image(url=req_url)
        await inter.followup.send(embed=embed)

    @meme.autocomplete("name")
    async def meme_autocomplete(self, inter: disnake.CommandInteraction, name: str):
        if not name:
            return list(self.memes.keys())[:20]
        completion = list()
        for meme_name in self.memes:
            if len(completion) == 20:
                break
            if name.lower() in meme_name.lower():
                completion.append(meme_name)
        return completion


def setup(bot: commands.Bot):
    bot.add_cog(MemefyCommand(bot))
