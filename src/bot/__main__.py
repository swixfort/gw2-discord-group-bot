""" Entry point """

from os import getenv
import logging
import discord
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """ bot ready message """
    logging.info('Logged in as %s', {client.user})

@client.event
async def on_message(message):
    """ reaction message to user """
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

if __name__ == "__main__":
    client.run(getenv("DISCORD_TOKEN"))
