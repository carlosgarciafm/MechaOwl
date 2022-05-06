import disnake
from disnake.ext import commands
from urllib import request
from json import loads
from random import choice


with request.urlopen("https://animechan.vercel.app/api/available/anime") as response:
    anime_list = loads(response.read())


class QuoteCommand(commands.Cog):
    """Quote an anime character using [Animechan](RocktimSaikia/anime-chan)."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.apiurl = "https://animechan.vercel.app/api"
        self.anime_list = anime_list

    @commands.slash_command()
    async def quote(
            self,
            inter: disnake.CommandInteraction,
            character: str | None = None,
            anime: str | None = None,
            ):
        """Quote an anime character.
        Parameters
        -----------
        character: character name to be quoted
        anime: anime name
        """
        req_url = self.apiurl
        if anime and character or character:
            req_url += f"/quotes/character?name={character.replace(' ', '.')}"
        elif anime:
            req_url += f"/quotes/anime?title={anime.replace(' ', '.')}"
        else:
            req_url +="/random"
        try:
            with request.urlopen(req_url) as response:
                answer = response.read()
                quote_dict = loads(answer)
        except:
            return await inter.response.send_message(
                    "An error occurred. Try later or with different names.")

        q = choice(quote_dict)

        embed = disnake.Embed(
                title=f"{q['character']} [{q['anime']}]:",
                description=f"***{q['quote']}***")
        embed.set_footer(text="Powered by Animechan API.")
        await inter.response.send_message(embed=embed)

    @quote.autocomplete("anime")
    async def anime_autocomplete(self, inter: disnake.CommandInteraction, name: str):
        if not name:
            return self.anime_list[:20]
        completion = list()
        for title in self.anime_list:
            if len(completion) == 20: break
            if name.lower() in title.lower():
                completion.append(title)
        return completion


def setup(bot: commands.Bot):
    bot.add_cog(QuoteCommand(bot))
