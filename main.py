import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import requests
import webserver

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
url = "https://api.thecatapi.com/v1/images/search"

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
#intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():

    try:
        sync = await bot.tree.sync()
        print("synced successfully")

    except Exception as e:
        print(e)

    print("Initializing CatRNG")


@bot.tree.command(name="rollcat", description="Roll a cat!")
async def generatebullshit(interaction):
    response = requests.get(url)

    if response.ok:
        phrase = response.json()[0]["url"]

        await interaction.response.send_message(phrase)
    else:
        await interaction.response.send_message(f"Couldn't roll a cat right now :( {response.status_code}")


webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
