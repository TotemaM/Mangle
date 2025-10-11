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

import nextcord
from nextcord.ext import commands
import const

class Mangle(commands.Bot):
    def __init__(self):
        super().__init__(intents=nextcord.Intents.all(),
                         command_prefix='/',
                         status=nextcord.Status.online,
                         owner_id=475354677773336596)
        self.guild: nextcord.Guild | None = None

    async def on_ready(self):
        self.guild = self.get_guild(const.GUILD_ID)
        if not self.guild:
            print(f"Not able to find guild with this id : {const.GUILD_ID}")
            exit(1)
        print(f"Application connected as {self.user.name}")