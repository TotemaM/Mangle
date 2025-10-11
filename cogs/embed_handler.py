################################################################################
#                                            __  __                   _        #
# cogs/embed_handler                        |  \/  |                 | |       #
#                                           | \  / | __ _ _ __   __ _| | ___   #
# MICHELETTI Matteo                         | |\/| |/ _` | '_ \ / _` | |/ _ \  #
# (https://github.com/TotemaM)              | |  | | (_| | | | | (_| | |  __/  #
#                                           |_|  |_|\__,_|_| |_|\__, |_|\___|  #
# This file is under MIT licence                                 __/ |         #
#                                                               |___/          #
################################################################################

import nextcord
from nextcord.ext import commands

from const import GUILD_ID
from ui.message import Message

def setup(mangle: commands.Bot):
    mangle.add_cog(MangleEmbedMessageHandler(mangle))

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

COLORS_DICT = {'white': 0xffffff, 'red': 0xff0000, 'burgundy': 0xb10000, 'orange': 0xff7000, 'gold': 0xffd300, 'yellow': 0xffed00 ,'lime': 0xbdff00, 'green': 0x08ff00,
                  'turquoise': 0x00ffa6, 'light_blue': 0x00e2ff, 'bleu': 0x00a3ff, 'dark_blue': 0x040fff, 'pink': 0xff80ff, 'violet': 0x8000ff, 'magenta': 0xff00ff,
                  'mauve': 0xd473d4, 'purple': 0xff0040, 'black': 0x000000, 'dark_grey': 0x575757, 'light_grey': 0xafafaf, 'old_discord': 0x7289da, 'discord': 0x5865f2,
                  'default': 0x2f3237}

COLORS_KEYS = [attribute.name for attribute in COLORS]

def create_embed(title=None,
                 description=None,
                 color: hex = COLORS.default,
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

class MangleEmbedMessageHandler(commands.Cog):
    def __init__(self, mangle: commands.Bot):
        self.mangle = mangle

    @nextcord.slash_command(name='message', description="Make the bot send an embed message in the current channel.")
    async def message(self, ia: nextcord.Interaction,
                      content: str = nextcord.SlashOption(name="outside", description="Content outside the embed message (Ping mentions here)", default=None, required=False),
                      title: str = nextcord.SlashOption(name="title", description="Embed title", default=None, required=False),
                      description: bool = nextcord.SlashOption(name="content", description="You want to add content inside the embed message ?", choices=[True, False], default=False, required=False),
                      color: str = nextcord.SlashOption(name="color", description="Embed color", choices=COLORS_KEYS, default="default", required=False),
                      link: str = nextcord.SlashOption(name="link", description="Transform the title to an clickable hyperlink.", default=None, required=False),
                      image: str = nextcord.SlashOption(name="image", description="Internet hyperlink to an image.", default=None, required=False),
                      thumbnail: str = nextcord.SlashOption(name="thumbnail", description="Internet hyperlink to an image.", default=None, required=False),
                      header_name: str = nextcord.SlashOption(name="header", description="Name shown at the top of the embed message", default=None, required=False),
                      header_icon: str = nextcord.SlashOption(name="avatar", description="Internet hyperlink to an image placed near the header name", default=None, required=False),
                      footer_name: str = nextcord.SlashOption(name="footer", description="Name displayed at the footer of the embed message", default=None, required=False),
                      footer_icon: str = nextcord.SlashOption(name="icon", description="Internet hyperlink to an image placed near the header name", default=None, required=False)):
        if description:
            await ia.response.send_modal(Message(embed=create_embed(title, None, COLORS_DICT[color], link, image, thumbnail, header_name, header_icon, footer_name, footer_icon), content=content, channel=ia.channel))
        else:
            try:
                message = await ia.channel.send(content=content, embed=create_embed(title, None, COLORS_DICT[color], link, image, thumbnail, header_name, header_icon, footer_name, footer_icon))
                await ia.send(content=f"Message send.\nMessage ID : `{message.id}`", ephemeral=True)
            except nextcord.errors.HTTPException:
                try:
                    message = await ia.channel.send(content=content)
                    await ia.send(content=f"Message send.\nMessage ID : `{message.id}`", ephemeral=True)
                except nextcord.errors.HTTPException:
                    await ia.send(content="Invalid message format", ephemeral=True)
                    return

    @nextcord.slash_command(name="message_edit", description="Allows to edit a previously send message from /message command")
    async def message_edit(self, ia: nextcord.Interaction,
                           message_id : str = nextcord.SlashOption(description="Message ID", required=True),
                           content: str = nextcord.SlashOption(name="outside", description="Content outside the embed message (Ping mentions here)", default=None, required=False),
                           title: str = nextcord.SlashOption(name="title", description="Embed title", default=None, required=False),
                           description: bool = nextcord.SlashOption(name="content", description="You want to edit the content inside the embed message ?", choices=[True, False], default=False, required=False),
                           color: str = nextcord.SlashOption(name="color", description="Embed color", choices=COLORS_KEYS, default="default", required=False),
                           link: str = nextcord.SlashOption(name="link", description="Transform the title to an clickable hyperlink.", default=None, required=False),
                           image: str = nextcord.SlashOption(name="image", description="Internet hyperlink to an image.", default=None, required=False),
                           thumbnail: str = nextcord.SlashOption(name="thumbnail", description="Internet hyperlink to an image.", default=None, required=False),
                           header_name: str = nextcord.SlashOption(name="header", description="Name shown at the top of the embed message", default=None, required=False),
                           header_icon: str = nextcord.SlashOption(name="avatar", description="Internet hyperlink to an image placed near the header name", default=None, required=False),
                           footer_name: str = nextcord.SlashOption(name="footer", description="Name displayed at the footer of the embed message", default=None, required=False),
                           footer_icon: str = nextcord.SlashOption(name="icon", description="Internet hyperlink to an image placed near the header name", default=None, required=False)):
        message = await ia.channel.get_partial_message(int(message_id)).fetch()
        if description:
            await ia.response.send_modal(Message(embed=create_embed(title, None, COLORS_DICT[color], link, image, thumbnail, header_name, header_icon, footer_name, footer_icon), content=content, channel=ia.channel, origin=message))
        else:
            try:
                await message.edit(content=content, embed=create_embed(title, None, COLORS_DICT[color], link, image, thumbnail, header_name, header_icon, footer_name, footer_icon))
                await ia.send(content="Modified message", ephemeral=True)
            except nextcord.errors.HTTPException:
                try:
                    await message.edit(content=content)
                    await ia.send(content="Modified message", ephemeral=True)
                except nextcord.errors.HTTPException:
                    await ia.send(content="Invalid message format", ephemeral=True)
                    return