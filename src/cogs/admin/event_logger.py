################################################################################
#                                            __  __                   _        #
# cogs/admin/event_logger.py                |  \/  |                 | |       #
#                                           | \  / | __ _ _ __   __ _| | ___   #
# MICHELETTI Matteo                         | |\/| |/ _` | '_ \ / _` | |/ _ \  #
# (https://github.com/TotemaM)              | |  | | (_| | | | | (_| | |  __/  #
#                                           |_|  |_|\__,_|_| |_|\__, |_|\___|  #
# This file is under MIT licence                                 __/ |         #
#                                                               |___/          #
################################################################################
from unittest import expectedFailure

import nextcord, const
from nextcord.ext import commands
from bot import Mangle
from cogs.admin.embed_message import create_embed, COLORS_DICT

def setup(mangle: commands.Bot):
    mangle.add_cog(MangleEventLogger(mangle))

class MangleEventLogger(commands.Cog):
    def __init__(self, mangle: Mangle):
        self.mangle = mangle

    """
    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        pass

    @commands.Cog.listener()
    async def on_member_remove(self, member: nextcord.Member):
        pass
    """
    @commands.Cog.listener()
    async def on_message(self, msg: nextcord.Message):
        if msg.author.id != self.mangle.user.id and const.BOT_CHANNEL_ID == msg.channel.id and \
                msg.type == nextcord.MessageType.default:
            await msg.delete()
        return

    @commands.Cog.listener()
    async def on_raw_message_delete(self, pl: nextcord.RawMessageDeleteEvent):
        channel = self.mangle.get_channel(pl.channel_id)
        if channel.category.id in const.NOT_LOGGED_CATEGORIES_IDS or channel.id == const.BOT_CHANNEL_ID:
            return
        cache = pl.cached_message
        if cache is not None:
            embed = create_embed(title="Message deleted :", color=COLORS_DICT['red'], description=f"Message send by {cache.author.mention} in {cache.channel.mention} has been deleted.")
            embed.add_field(name="Message content :", value=f"```{cache.content} ```", inline=False)
            await self.mangle.LOG_CHANNEL.send(embed=embed)
        else:
            await self.mangle.LOG_CHANNEL.send(embed=create_embed(color=COLORS_DICT['red'], title="Message deleted :", description="Unable to fetch message data."))

    @commands.Cog.listener()
    async def on_raw_message_edit(self, pl: nextcord.RawMessageUpdateEvent):
        channel = self.mangle.get_channel(int(pl.channel_id))
        cache = pl.cached_message
        if channel.category.id in const.NOT_LOGGED_CATEGORIES_IDS or cache.author.id == self.mangle.user.id:
            return
        message = await channel.fetch_message(int(pl.message_id))
        if cache is not None:
            embed = create_embed(title="Message edited :", color=COLORS_DICT['yellow'], description=f"Message send by{cache.author.mention} in {cache.channel.mention} has been modified.")
            embed.add_field(name="Content before modification :", value=f"```{cache.content} ```", inline=False)
            embed.add_field(name="Content after modification :", value=f"```{message.content} ```", inline=False)
            await self.mangle.LOG_CHANNEL.send(embed=embed)
        else:
            await self.mangle.LOG_CHANNEL.send(embed=create_embed(color=COLORS_DICT['yellow'], title="Message modified :", description="Unable to fetch message data."))

    @commands.Cog.listener()
    async def on_application_command_error(self, ia: nextcord.Interaction, exception):
        return await self.mangle.LOG_CHANNEL.send(embed=create_embed(title="Application command error", fields=(("User :", ia.user.mention, False), ("Exception :", str(exception), False)), icon=ia.user.display_avatar, color=COLORS_DICT['light_blue']))

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, exception):
        return await self.mangle.LOG_CHANNEL.send(embed=create_embed(title="Command error", fields=(("User :", ctx.author.mention, False), ("Exception :", str(exception), False)), icon=ctx.author.display_avatar, color=COLORS_DICT['blue']))