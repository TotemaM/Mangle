################################################################################
#                                            __  __                   _        #
# main.py                                   |  \/  |                 | |       #
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

mangle = commands.Bot(intents=nextcord.Intents.all(),
                      command_prefix=' ',
                      activity=nextcord.Activity(name="/help", type=nextcord.ActivityType.playing),
                      status=nextcord.Status.online,
                      owner_id=475354677773336596)

for cog in ["embed_handler"]:
    mangle.load_extension(f"cogs.{cog}")

mangle.run(const.APP_TOKEN)
