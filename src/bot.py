################################################################################
#                                            __  __                   _        #
# bot.py                                    |  \/  |                 | |       #
#                                           | \  / | __ _ _ __   __ _| | ___   #
# MICHELETTI Matteo                         | |\/| |/ _` | '_ \ / _` | |/ _ \  #
# (https://github.com/TotemaM)              | |  | | (_| | | | | (_| | |  __/  #
#                                           |_|  |_|\__,_|_| |_|\__, |_|\___|  #
# This file is under MIT licence                                 __/ |         #
#                                                               |___/          #
################################################################################

import nextcord, const
from nextcord.ext import commands

class Mangle(commands.Bot):
    def __init__(self):
        super().__init__(intents=nextcord.Intents.all(), command_prefix='/', status=nextcord.Status.online,
                         owner_id=475354677773336596, help_command=None)
        self.guild: nextcord.Guild | None = None
        self.BDE_NOTIFY_ROLE: nextcord.Role | None = None
        self.LOG_CHANNEL: nextcord.TextChannel | None = None

    async def on_ready(self):
        self.guild = self.get_guild(const.GUILD_ID)
        self.BDE_NOTIFY_ROLE = self.guild.get_role(const.BDE_NOTIFY_ROLE_ID)
        self.LOG_CHANNEL = self.guild.get_channel(const.LOG_CHANNEL_ID)
        if not self.guild or not self.BDE_NOTIFY_ROLE or not self.LOG_CHANNEL:
            print("Not able to load one of the constant guild variables")
            exit(1)
        print(f"Application connected as {self.user.name}")