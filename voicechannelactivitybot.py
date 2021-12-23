import os

import discord
from dotenv import load_dotenv


class VoiceChannelActivityBot(discord.Client):
    """
        Inherits from discord.py library implementation of a discord client
    """

    def __init__(self):
        """
            Loads the environment variables from a local .env file
            Then constructs a typical discord client
        """

        # load server (guild) name and authentication token
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.GUILD = os.getenv('DISCORD_GUILD')

        # Use the parent constructor to construct the client
        super().__init__()


    async def on_ready(self):
        """
            Prints a message to stdout when the bot is connected
            to the server and ready to operate.
        """
        guild = discord.utils.get(self.guilds, name=self.GUILD)
        print (
            f'{self.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

    def run(self):
        """
            Encapuslates the parent classes run method with
            an overriden version   
        """
        super().run(self.TOKEN)
