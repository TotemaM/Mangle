################################################################################
#                                            __  __                   _        #
# client.py                                 |  \/  |                 | |       #
#                                           | \  / | __ _ _ __   __ _| | ___   #
# MICHELETTI Matteo                         | |\/| |/ _` | '_ \ / _` | |/ _ \  #
# (https://github.com/TotemaM)              | |  | | (_| | | | | (_| | |  __/  #
#                                           |_|  |_|\__,_|_| |_|\__, |_|\___|  #
# This file is under MIT licence                                 __/ |         #
#                                                               |___/          #
################################################################################

from discord.ext import commands
import const

class Client(commands.Bot):
    async def on_ready(self):
        print(f"Connected as {self.user} with ID : {self.user.id}")
        try:
            synced = await self.tree.sync(guild=const.GUILD)
            print(f"{len(synced)} commands")
        except Exception as e:
            print(f"Error syncing {e}")