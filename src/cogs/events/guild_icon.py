################################################################################
#                                            __  __                   _        #
# cogs/events/guild_icon.py                 |  \/  |                 | |       #
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
from datetime import datetime

def setup(mangle: commands.Bot):
    mangle.add_cog(MangleGuildIconHandler(mangle))

class MangleGuildIconHandler(commands.Cog):
    def __init__(self, mangle: Mangle):
        self.mangle = mangle
        self.current = ""
        self.decay_loop = False

    @commands.Cog.listener()
    async def on_ready(self):
        await self.cycle_guild_icon.start()

    async def _set_guild_icon(self, path: str):
        if path == self.current:
            return
        with open(path, "rb") as img:
            await self.mangle.guild.edit(icon=img.read())
        self.current = path

    @tasks.loop(hours=8)
    async def cycle_guild_icon(self):
        if not self.decay_loop:
            self.decay_loop = True
            return
        dt = datetime.now()
        if datetime(year= dt.year, month=10, day=25) <= dt <= datetime(year=dt.year, month=11, day=2):
            await self._set_guild_icon("static/guild_icons/halloween.png")
        else:
            await self._set_guild_icon("static/guild_icons/default.png")
