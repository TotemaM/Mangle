################################################################################
#                                            __  __                   _        #
# cogs/command_utils.py                     |  \/  |                 | |       #
#                                           | \  / | __ _ _ __   __ _| | ___   #
# MICHELETTI Matteo                         | |\/| |/ _` | '_ \ / _` | |/ _ \  #
# (https://github.com/TotemaM)              | |  | | (_| | | | | (_| | |  __/  #
#                                           |_|  |_|\__,_|_| |_|\__, |_|\___|  #
# This file is under MIT licence                                 __/ |         #
#                                                               |___/          #
################################################################################

import nextcord
from bot import Mangle
import const


async def check_bot_channel(mangle: Mangle, ia: nextcord.Interaction):
	if ia.channel.id != const.BOT_CHANNEL_ID:
		await ia.send(
			content=f"You're not in the appropriate channel, try this here {mangle.get_channel(const.BOT_CHANNEL_ID).mention}",
			ephemeral=True, delete_after=5)
		return 0
	return 1
