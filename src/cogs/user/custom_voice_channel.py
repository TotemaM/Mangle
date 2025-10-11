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

import nextcord, const
from nextcord.ext import commands, tasks

def setup(mangle: commands.Bot):
    mangle.add_cog(MangleCustomVoiceChannel(mangle))

class MangleCustomVoiceChannel(commands.Cog):
    def __init__(self, mangle: commands.Bot):
        self.mangle = mangle
        self.custom_voice_channels: list[nextcord.VoiceChannel] = []

    @commands.Cog.listener()
    async def on_ready(self):
        await self.check_custom_voice_channels.start()

    @tasks.loop(minutes=1)
    async def check_custom_voice_channels(self):
        for voice_channel in self.custom_voice_channels:
            if len(voice_channel.members) == 0:
                try:
                    await voice_channel.delete()
                except nextcord.NotFound:
                    pass
                self.custom_voice_channels.remove(voice_channel)

    @nextcord.slash_command(name="create_voice_channel", description="Go into a voice channel and type this command to create your temporary voice channel.")
    async def custom_vc(self, ia: nextcord.Interaction, channel_name: str = nextcord.SlashOption(required=True)):
        if ia.channel.id != const.BOT_CHANNEL_ID:
            return await ia.send(content=f"You're not in the appropriate channel, try this here {self.mangle.get_channel(const.BOT_CHANNEL_ID).mention}", ephemeral=True)
        if not ia.user.voice:
            return await ia.send(content="You have to be in a voice channel to create a yours.", ephemeral=True)
        new_voice_channel = await ia.user.voice.channel.category.create_voice_channel(name=f"💠・{channel_name}")
        self.custom_voice_channels.append(new_voice_channel)
        await ia.user.move_to(new_voice_channel)
        await new_voice_channel.set_permissions(target=ia.user, overwrite=nextcord.PermissionOverwrite(manage_channels=True, manage_permissions=True, connect=True))
        return await ia.send(content="Voice channel created", ephemeral=True, delete_after=5)
