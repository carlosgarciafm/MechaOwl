# MechaOwl
This is a general purpose discord bot built using the
[disnake](https://docs.disnake.dev/en/latest/) API.


# Configuration
This bot reads the following values as environment variables:
* `MECHAOWL_TOKEN`: discord application token generated via the official discord
  site,
* `MECHAOWL_GUILDID`: id of the server (internally known as guild) you want to
  bot to run in.

The local setup process as straight forward as installing the required packages
(preferably within a python virtual environment) and run the `MechaOwl.py`
python script.

```sh
pip install -r requirements.txt     # install dependencies
python MechaOwl.py                  # run the script
```


# Acknowledgements
This bot depends on a few APIs to work correctly:
* [disnake](https://docs.disnake.dev/en/latest/): main API to interact with
  discord,
* [memegen](https://github.com/jacebrowning/memegen): to create and retrieve a
  great variety of memes,
* [Animechan](https://github.com/RocktimSaikia/anime-chan): to fetch quotes from
  anime characters.
