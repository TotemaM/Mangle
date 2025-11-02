################################################################################
#                                            __  __                   _        #
# cogs/admin/qr_code.py                     |  \/  |                 | |       #
#                                           | \  / | __ _ _ __   __ _| | ___   #
# MICHELETTI Matteo                         | |\/| |/ _` | '_ \ / _` | |/ _ \  #
# (https://github.com/TotemaM)              | |  | | (_| | | | | (_| | |  __/  #
#                                           |_|  |_|\__,_|_| |_|\__, |_|\___|  #
# This file is under MIT licence                                 __/ |         #
#                                                               |___/          #
################################################################################

import nextcord
from qrcode.main import QRCode
from qrcode import constants as qr_const
from nextcord.ext import commands
from bot import Mangle
from command_utils import check_bot_channel
import os

ERROR_CORR = {"7": qr_const.ERROR_CORRECT_L,
              "15": qr_const.ERROR_CORRECT_M,
              "25": qr_const.ERROR_CORRECT_Q,
              "30": qr_const.ERROR_CORRECT_H}


def setup(mangle: commands.Bot):
	mangle.add_cog(MangleQRCode(mangle))


class MangleQRCode(commands.Cog):
	def __init__(self, mangle: Mangle):
		self.mangle = mangle

	@nextcord.slash_command(name="qrcode", description="Create a QR code.", default_member_permissions=8)
	async def qrcode_command(self, ia: nextcord.Interaction,
	                         content: str = nextcord.SlashOption(required=True),
	                         version: int = nextcord.SlashOption(min_value=1, max_value=50, required=False),
	                         unit_size: int = nextcord.SlashOption(min_value=1, max_value=100, required=False,
	                                                               default=10),
	                         border_size: int = nextcord.SlashOption(min_value=0, max_value=20, required=False,
	                                                                 default=4),
	                         err_corr_perc: str = nextcord.SlashOption(name="redundancy",
	                                                                   description="Percentage of redundancy",
	                                                                   required=False, default="15",
	                                                                   choices=["7", "15", "25", "30"])):
		if not await check_bot_channel(self.mangle, ia):
			return
		filename = f"static/qrcode_{ia.user.name}.png"
		qr_code = QRCode()
		if version:
			qr_code.version = version
		if unit_size:
			qr_code.size = unit_size
		if border_size:
			qr_code.border = border_size
		if err_corr_perc:
			qr_code.error_correction = int(ERROR_CORR[err_corr_perc])
		qr_code.add_data(content)
		qr_code.make(fit=True)
		qr_image = qr_code.make_image()
		qr_image.save(filename)
		await ia.send(file=nextcord.File(filename), ephemeral=True)
		os.remove(filename)
		return
