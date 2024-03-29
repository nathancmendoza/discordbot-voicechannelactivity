"""
    :module_name: vca_bot
    :module_summary: A discord bot that monitors and announces voice channel activity in a server
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""
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
        self.token = os.getenv('DISCORD_TOKEN')
        self.server = os.getenv('DISCORD_GUILD')
        self.log = None
        self.logname = 'vcalog'
        self._intents = discord.Intents(messages=True, guilds=True)

        # Use the parent constructor to construct the client
        super().__init__(intents = self._intents)


    async def create_log_channel(self, guild):
        """
            asynchronous method for creating a text channel
            for the discord client to send its announcements.
            If it already exists, use that channel instead
        """
        if all(c.name != self.logname for c in guild.channels):
            self.log = await guild.create_text_channel(self.logname)
        else:
            # if we get here, the log channel should already exist. Find it.
            for channel in guild.channels:
                if channel.name == self.logname:
                    self.log = channel
                    break


    async def on_ready(self):
        """
            Prints a message to stdout when the bot is connected
            to the server and ready to operate.
        """
        guild = discord.utils.get(self.guilds, name=self.server)
        await self.create_log_channel(guild)
        print (
            f'{self.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


    async def handle_voice_channel_enter(self, member):
        """
            Implements what should happen if a member joins a voice channel
        """
        vcamessage = f'{member.name} has joined {member.voice.channel}'
        await self.log.send(vcamessage)

    async def handle_voice_channel_exit(self, member, channelleft):
        """
            Implements what should happen if a member leaves a voice channel
        """
        vcamessage = f'{member.name} has left {channelleft}'
        await self.log.send(vcamessage)


    async def on_voice_state_update(self, member, before, after):
        """
            Implements the high level interface of voice state change events
        """
        if before.channel is None and after.channel is not None:
            await self.handle_voice_channel_enter(member)
        if before.channel is not None and after.channel is None:
            await self.handle_voice_channel_exit(member, before.channel)


    def run(self):
        """
            Encapuslates the parent classes run method with
            an overriden version
        """
        super().run(self.token)
