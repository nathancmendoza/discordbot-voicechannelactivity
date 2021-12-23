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
        self.log = None
        self.logname = 'vcalog'

        # Use the parent constructor to construct the client
        super().__init__()


    async def on_ready(self):
        """
            Prints a message to stdout when the bot is connected
            to the server and ready to operate.
        """
        guild = discord.utils.get(self.guilds, name=self.GUILD)
        if all([c.name != self.logname for c in guild.channels]):
            self.log = await guild.create_text_channel(self.logname)
        
        print (
            f'{self.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

    async def handle_voice_channel_join(member):
        pass
        

    async def handle_voice_channel_leave(member):
        pass


    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            await handle_voice_channel_join(member)
        if before.channel is not None and after.channel is None:
            await handle_voice_channel_leave(member)


    def run(self):
        """
            Encapuslates the parent classes run method with
            an overriden version   
        """
        super().run(self.TOKEN)
