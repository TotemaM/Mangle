################################################################################
#                                            __  __                   _        #
# cogs/admin/embed_message.py               |  \/  |                 | |       #
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
from command_utils import create_embed, log_command, COLORS_KEYS


def setup(mangle: commands.Bot):
	mangle.add_cog(MangleEmbedMessageHandler(mangle))


class EmbedMessageModal(nextcord.ui.Modal):
	def __init__(self, embed: nextcord.Embed, content: str, channel: nextcord.TextChannel, origin=False):
		super().__init__(title="Embed message creator", timeout=300)
		self.content = content
		self.description = nextcord.ui.TextInput(label="Content", placeholder="...",
		                                         style=nextcord.TextInputStyle.paragraph, required=True, min_length=1,
		                                         max_length=3968)
		self.add_item(self.description)
		self.embed = embed
		self.channel = channel
		self.origin = origin

	async def callback(self, ia: nextcord.Interaction):
		self.embed.description = self.description.value
		if self.origin:
			if self.content:
				await self.origin.edit(content=self.content, embed=self.embed)
			else:
				await self.origin.edit(embed=self.embed)
			await ia.send(content="Message edited", delete_after=5.0)
		else:
			if self.content:
				message = await self.channel.send(content=self.content, embed=self.embed)
			else:
				message = await self.channel.send(embed=self.embed)
			await ia.send(content=f"Message ID : `{message.id}`", ephemeral=True, delete_after=10)


class MangleEmbedMessageHandler(commands.Cog):
	def __init__(self, mangle: Mangle):
		self.mangle = mangle

	@nextcord.slash_command(name='message', description="Make the bot send an embed message in the current channel.",
	                        default_member_permissions=8)
	async def message(self, ia: nextcord.Interaction,
	                  content: str = nextcord.SlashOption(name="outside",
	                                                      description="Content outside the embed message (Ping mentions here)",
	                                                      default=None, required=False),
	                  title: str = nextcord.SlashOption(name="title", description="Embed title", default=None,
	                                                    required=False),
	                  description: bool = nextcord.SlashOption(name="content",
	                                                           description="You want to add content inside the embed message ?",
	                                                           choices=[True, False], default=False, required=False),
	                  color: str = nextcord.SlashOption(name="color", description="Embed color", choices=COLORS_KEYS,
	                                                    default="default", required=False),
	                  link: str = nextcord.SlashOption(name="link",
	                                                   description="Transform the title to an clickable hyperlink.",
	                                                   default=None, required=False),
	                  image: str = nextcord.SlashOption(name="image", description="Internet hyperlink to an image.",
	                                                    default=None, required=False),
	                  thumbnail: str = nextcord.SlashOption(name="thumbnail",
	                                                        description="Internet hyperlink to an image.", default=None,
	                                                        required=False),
	                  header_name: str = nextcord.SlashOption(name="header",
	                                                          description="Name shown at the top of the embed message",
	                                                          default=None, required=False),
	                  header_icon: str = nextcord.SlashOption(name="avatar",
	                                                          description="Internet hyperlink to an image placed near the header name",
	                                                          default=None, required=False),
	                  footer_name: str = nextcord.SlashOption(name="footer",
	                                                          description="Name displayed at the footer of the embed message",
	                                                          default=None, required=False),
	                  footer_icon: str = nextcord.SlashOption(name="icon",
	                                                          description="Internet hyperlink to an image placed near the header name",
	                                                          default=None, required=False)):
		await log_command(self.mangle, ia, "message")
		if description:
			try:
				await ia.response.send_modal(modal=EmbedMessageModal(
					embed=create_embed(title, None, COLORS_DICT[color], link, image, thumbnail, header_name,
					                   header_icon, footer_name, footer_icon), content=content, channel=ia.channel))
			except nextcord.errors.HTTPException:
				return await ia.send(content="Invalid message format", ephemeral=True)
		else:
			try:
				await ia.channel.send(content=content,
				                      embed=create_embed(title, None, COLORS_DICT[color], link, image, thumbnail,
				                                         header_name, header_icon, footer_name, footer_icon))
			except nextcord.errors.HTTPException:
				try:
					await ia.channel.send(content=content)
				except nextcord.errors.HTTPException:
					return await ia.send(content="Invalid message format", ephemeral=True)
		return await ia.send("Message send", ephemeral=True, delete_after=5)

	@nextcord.slash_command(name="message_edit",
	                        description="Allows to edit a previously send message from /message command",
	                        default_member_permissions=8)
	async def message_edit(self, ia: nextcord.Interaction,
	                       message_id: str = nextcord.SlashOption(name="message_id", description="Message ID",
	                                                              required=True),
	                       content: str = nextcord.SlashOption(name="outside",
	                                                           description="Content outside the embed message (Ping mentions here)",
	                                                           default=None, required=False),
	                       title: str = nextcord.SlashOption(name="title", description="Embed title", default=None,
	                                                         required=False),
	                       description: bool = nextcord.SlashOption(name="content",
	                                                                description="You want to edit the content inside the embed message ?",
	                                                                choices=[True, False], default=False,
	                                                                required=False),
	                       color: str = nextcord.SlashOption(name="color", description="Embed color",
	                                                         choices=COLORS_KEYS, default="default", required=False),
	                       link: str = nextcord.SlashOption(name="link",
	                                                        description="Transform the title to an clickable hyperlink.",
	                                                        default=None, required=False),
	                       image: str = nextcord.SlashOption(name="image",
	                                                         description="Internet hyperlink to an image.",
	                                                         default=None, required=False),
	                       thumbnail: str = nextcord.SlashOption(name="thumbnail",
	                                                             description="Internet hyperlink to an image.",
	                                                             default=None, required=False),
	                       header_name: str = nextcord.SlashOption(name="header",
	                                                               description="Name shown at the top of the embed message",
	                                                               default=None, required=False),
	                       header_icon: str = nextcord.SlashOption(name="avatar",
	                                                               description="Internet hyperlink to an image placed near the header name",
	                                                               default=None, required=False),
	                       footer_name: str = nextcord.SlashOption(name="footer",
	                                                               description="Name displayed at the footer of the embed message",
	                                                               default=None, required=False),
	                       footer_icon: str = nextcord.SlashOption(name="icon",
	                                                               description="Internet hyperlink to an image placed near the header name",
	                                                               default=None, required=False)):
		await log_command(self.mangle, ia, "message_edit")
		message = await ia.channel.get_partial_message(int(message_id)).fetch()
		if description:
			return await ia.response.send_modal(EmbedMessageModal(
				embed=create_embed(title, None, COLORS_DICT[color], link, image, thumbnail, header_name, header_icon,
				                   footer_name, footer_icon), content=content, channel=ia.channel, origin=message))
		else:
			try:
				await message.edit(content=content,
				                   embed=create_embed(title, None, COLORS_DICT[color], link, image, thumbnail,
				                                      header_name, header_icon, footer_name, footer_icon))
				return await ia.send(content="Message has been edited", ephemeral=True, delete_after=5)
			except nextcord.errors.HTTPException:
				try:
					return await message.edit(content=content)
				except nextcord.errors.HTTPException:
					return await ia.send(content="Invalid message format", ephemeral=True)
