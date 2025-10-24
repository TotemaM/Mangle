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

from bot import Mangle
import const

if __name__ == '__main__':
    mangle = Mangle()
    cogs = [
        "admin.event_logger",
        "admin.embed_message",
        "events.guild_icon",
        "user.custom_voice_channel",
        "user.request_staff"
    ]
    for cog in cogs:
        mangle.load_extension(f"cogs.{cog}")
    mangle.run(const.APP_TOKEN)
