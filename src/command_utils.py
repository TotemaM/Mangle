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
import enum


class COLORS(enum.Enum):
	white = 0xffffff
	red = 0xff0000
	burgundy = 0xb10000
	orange = 0xff7000
	gold = 0xffd300
	yellow = 0xffed00
	lime = 0xbdff00
	green = 0x08ff00
	turquoise = 0x00ffa6
	light_blue = 0x00e2ff
	bleu = 0x00a3ff
	dark_blue = 0x040fff
	pink = 0xff80ff
	violet = 0x8000ff
	magenta = 0xff00ff
	mauve = 0xd473d4
	purple = 0xff0040
	black = 0x000000
	dark_grey = 0x575757
	light_grey = 0xafafaf
	old_discord = 0x7289da
	discord = 0x5865f2
	default = 0x2f3237


COLORS_DICT = {'white': 0xffffff, 'red': 0xff0000, 'burgundy': 0xb10000, 'orange': 0xff7000, 'gold': 0xffd300,
               'yellow': 0xffed00, 'lime': 0xbdff00, 'green': 0x08ff00,
               'turquoise': 0x00ffa6, 'light_blue': 0x00e2ff, 'blue': 0x00a3ff, 'dark_blue': 0x040fff, 'pink': 0xff80ff,
               'violet': 0x8000ff, 'magenta': 0xff00ff,
               'mauve': 0xd473d4, 'purple': 0xff0040, 'black': 0x000000, 'dark_grey': 0x575757, 'light_grey': 0xafafaf,
               'old_discord': 0x7289da, 'discord': 0x5865f2,
               'default': 0x2f3237}

COLORS_KEYS = [attribute.name for attribute in COLORS]


def create_embed(title=None,
                 description=None,
                 color: hex = COLORS_DICT['default'],
                 link=None,
                 image=None,
                 icon=None,
                 header=None,
                 header_icon=None,
                 footer=None,
                 footer_icon=None,
                 fields: tuple = ()):
	message = nextcord.Embed()
	if title is not None:
		message.title = title
	if description is not None:
		message.description = description
	if color is not None:
		message.colour = color
	if link is not None:
		message.url = link
	if image is not None:
		message.set_image(url=str(image))
	if icon is not None:
		message.set_thumbnail(url=str(icon))
	if header_icon is not None:
		message.set_author(name=header, icon_url=str(header_icon))
	elif header is not None:
		message.set_author(name=header)
	if footer_icon is not None:
		message.set_footer(text=footer, icon_url=str(footer_icon))
	elif footer is not None:
		message.set_footer(text=footer)
	for field in fields:
		if len(field) == 3:
			message.add_field(name=field[0], value=field[1], inline=field[2])
		else:
			message.add_field(name=field[0], value=field[1], inline=True)
	return message

async def check_bot_channel(mangle: Mangle, ia: nextcord.Interaction):
	if ia.channel.id != const.BOT_CHANNEL_ID:
		await ia.send(
			content=f"You're not in the appropriate channel, try this here {mangle.get_channel(const.BOT_CHANNEL_ID).mention}",
			ephemeral=True, delete_after=5)
		return 0
	return 1

async def log_command(mangle: Mangle, ia: nextcord.Interaction, command_name: str):
	await mangle.LOG_CHANNEL.send(embed=create_embed(color=COLORS_DICT['light_blue'], title=f"`/{command_name}` command typed",
	                                                 icon=ia.user.display_avatar,
	                                                 fields=(("User", f"{ia.user.mention}", 0),
	                                                         ("Channel", f"{ia.channel.mention}", 0))))
