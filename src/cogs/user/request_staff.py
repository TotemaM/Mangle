################################################################################
#                                            __  __                   _        #
# cogs/user/request_staff.py                |  \/  |                 | |       #
#                                           | \  / | __ _ _ __   __ _| | ___   #
# MICHELETTI Matteo                         | |\/| |/ _` | '_ \ / _` | |/ _ \  #
# (https://github.com/TotemaM)              | |  | | (_| | | | | (_| | |  __/  #
#                                           |_|  |_|\__,_|_| |_|\__, |_|\___|  #
# This file is under MIT licence                                 __/ |         #
#                                                               |___/          #
################################################################################

import nextcord, const
from nextcord.ext import commands
from bot import Mangle
from cogs.admin.embed_message import create_embed, COLORS_DICT


def setup(mangle: commands.Bot):
	mangle.add_cog(MangleRequestStaff(mangle))


REQUEST_TYPES = ["Club", "Event", "Generic"]


class RequestStaffView(nextcord.ui.View):
	def __init__(self, message: nextcord.Message, channel: nextcord.TextChannel, embed: nextcord.Embed):
		super().__init__()
		self.msg = message
		self.channel = channel
		self.embed = embed

	@nextcord.ui.button(label="Close request", style=nextcord.ButtonStyle.red)
	async def close_request(self, button: nextcord.ui.Button, ia: nextcord.Interaction):
		self.embed.set_footer(text=f"This request was closed by {ia.user.display_name}", icon_url=ia.user.avatar.url)
		self.embed.colour = COLORS_DICT['default']
		self.embed.remove_field(0)
		await self.msg.edit(embed=self.embed, view=None)
		await self.channel.delete()
		self.stop()


class RequestStaffModal(nextcord.ui.Modal):
	def __init__(self, title, channel: nextcord.TextChannel, category: nextcord.CategoryChannel, request_type: str,
	             notify_role: nextcord.Role):
		super().__init__(title=title)
		self.channel = channel
		self.category = category
		self.request_type = request_type
		self.notify_role = notify_role
		self.description = nextcord.ui.TextInput(label="Short description of your request", placeholder="",
		                                         style=nextcord.TextInputStyle.paragraph, required=True, min_length=1,
		                                         max_length=3968)
		self.add_item(self.description)

	async def callback(self, ia: nextcord.Interaction):
		new_text_channel = await self.category.create_text_channel(name=f"{ia.user.display_name}")
		await new_text_channel.set_permissions(target=ia.user,
		                                       overwrite=nextcord.PermissionOverwrite(view_channel=True))
		embed: nextcord.Embed = create_embed(title=f"{self.request_type} request by {ia.user.display_name}",
		                                     description=self.description.value, icon=ia.user.display_avatar,
		                                     fields=(("Follow up channel", f"{new_text_channel.mention}"),))
		msg = await self.channel.send(content="...")
		view: nextcord.ui.View = RequestStaffView(msg, new_text_channel, embed)
		match self.request_type:
			case "Club":
				await new_text_channel.edit(name=f"🔹{ia.user.display_name}")
				embed.colour = COLORS_DICT['blue']
				await msg.edit(content=f"{self.notify_role.mention} new club request by {ia.user.mention}", embed=embed,
				               view=view)
			case "Event":
				await new_text_channel.edit(name=f"🔸{ia.user.display_name}")
				embed.colour = COLORS_DICT['orange']
				await msg.edit(content=f"{self.notify_role.mention} new event request by {ia.user.mention}",
				               embed=embed, view=view)
			case "Generic":
				await new_text_channel.edit(name=f"▫️{ia.user.display_name}")
				embed.colour = COLORS_DICT['white']
				await msg.edit(content=f"{self.notify_role.mention} new request by {ia.user.mention}", embed=embed,
				               view=view)
		return await new_text_channel.send(
			content=f"{ia.user.mention}, your {self.request_type} request will be followed up here : \n\n{self.description.value}")


class MangleRequestStaff(commands.Cog):
	def __init__(self, mangle: Mangle):
		self.mangle = mangle

	@nextcord.slash_command(name="request_bde",
	                        description="Make a request to the BDE. Your request will be followed by the BDE staff")
	async def request_bde(self, ia: nextcord.Interaction,
	                      request_type: str = nextcord.SlashOption(required=True, choices=REQUEST_TYPES)):
		if ia.channel.id != const.BOT_CHANNEL_ID:
			return await ia.send(
				content=f"You're not in the appropriate channel, try this here {self.mangle.get_channel(const.BOT_CHANNEL_ID).mention}",
				ephemeral=True, delete_after=5)
		request_channel: nextcord.TextChannel = self.mangle.guild.get_channel(const.REQUEST_CHANNEL_ID)
		return await ia.response.send_modal(
			RequestStaffModal(title=f"{request_type} request", request_type=request_type, channel=request_channel,
			                  category=request_channel.category, notify_role=self.mangle.BDE_NOTIFY_ROLE))
