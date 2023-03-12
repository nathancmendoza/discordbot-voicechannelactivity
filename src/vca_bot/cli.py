"""
    :module_name: cli
    :module_summary: a CLI for vca_bot
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import click

from . import VoiceChannelActivityBot

@click.command()
def VCABot():
    """Entry point to VCABot"""
    VoiceChannelActivityBot().run()
