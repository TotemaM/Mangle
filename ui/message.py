################################################################################
#                                            __  __                   _        #
# ui/message.py                             |  \/  |                 | |       #
#                                           | \  / | __ _ _ __   __ _| | ___   #
# MICHELETTI Matteo                         | |\/| |/ _` | '_ \ / _` | |/ _ \  #
# (https://github.com/TotemaM)              | |  | | (_| | | | | (_| | |  __/  #
#                                           |_|  |_|\__,_|_| |_|\__, |_|\___|  #
# This file is under MIT licence                                 __/ |         #
#                                                               |___/          #
################################################################################

import nextcord

class Message(nextcord.ui.Modal):
    def __init__(self, embed: nextcord.Embed, content: str, channel: nextcord.TextChannel, origin=False):
        super().__init__(title="Message content :")
        self.content = content
        self.description = nextcord.ui.TextInput(label="", placeholder="",
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
            await ia.send(content=f"Message send.\nMessage ID : `{message.id}`", ephemeral=True)