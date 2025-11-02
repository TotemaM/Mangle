################################################################################
#                                            __  __                   _        #
# cogs/user/custom_voice_channel.py         |  \/  |                 | |       #
#                                           | \  / | __ _ _ __   __ _| | ___   #
# MICHELETTI Matteo                         | |\/| |/ _` | '_ \ / _` | |/ _ \  #
# (https://github.com/TotemaM)              | |  | | (_| | | | | (_| | |  __/  #
#                                           |_|  |_|\__,_|_| |_|\__, |_|\___|  #
# This file is under MIT licence                                 __/ |         #
#                                                               |___/          #
################################################################################

import nextcord
from nextcord.ext import commands, tasks
from bot import Mangle
from command_utils import check_bot_channel


def setup(mangle: commands.Bot):
	mangle.add_cog(MangleCustomVoiceChannel(mangle))


class MangleCustomVoiceChannel(commands.Cog):
	def __init__(self, mangle: Mangle):
		self.mangle = mangle
		self.custom_voice_channels: list[nextcord.VoiceChannel] = []
		self.SAVE_FILE = "static/voice_channel.save"
		try:
			open(self.SAVE_FILE, "x")
		except FileExistsError:
			pass

	def add_channel(self, channel: nextcord.VoiceChannel):
		self.custom_voice_channels.append(channel)
		with open(self.SAVE_FILE, "a") as file:
			file.write(f"{channel.id}\n")

	def save_channels(self):
		with (open(self.SAVE_FILE, "w") as file):
			for vc in self.custom_voice_channels:
				file.write(f"{vc.id}\n")

	@commands.Cog.listener()
	async def on_ready(self):
		with open(self.SAVE_FILE, "r") as file:
			for line in file:
				channel = self.mangle.get_channel(int(line))
				if channel is not None:
					self.custom_voice_channels.append(channel)
		await self.check_custom_voice_channels.start()

	@tasks.loop(minutes=1)
	async def check_custom_voice_channels(self):
		new_list = []
		for voice_channel in self.custom_voice_channels:
			if len(voice_channel.members) == 0:
				try:
					await voice_channel.delete()
				except nextcord.NotFound:
					pass
			else:
				new_list.append(voice_channel)
		self.custom_voice_channels = new_list
		self.save_channels()

	@nextcord.slash_command(name="create_voice_channel",
	                        description="Go into a voice channel and type this command to create your temporary voice channel.")
	async def custom_vc(self, ia: nextcord.Interaction,
	                    channel_name: str = nextcord.SlashOption(required=True, min_length=2, max_length=12)):
		if not await check_bot_channel(self.mangle, ia):
			return
		if not ia.user.voice:
			await ia.send(content="You have to be in a voice channel to create a yours.", ephemeral=True)
			return
		new_voice_channel = await ia.user.voice.channel.category.create_voice_channel(
			name=f"💠・{"".join(c.lower() for c in channel_name if c.isalpha())}")
		self.add_channel(new_voice_channel)
		await ia.send(content="Voice channel created", ephemeral=True, delete_after=5)
		await ia.user.move_to(new_voice_channel)
		return
