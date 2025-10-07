import discord
from discord.ext import commands
import const

class Client(commands.Bot):
    async def on_ready(self):
        print(f"Connected as {self.user} with ID : {self.user.id}")
        try:
            synced = await self.tree.sync(guild=const.GUILD)
            print(f"{len(synced)} commands")
        except Exception as e:
            print(f"Error syncing {e}")