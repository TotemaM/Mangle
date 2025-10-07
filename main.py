import discord
import const
from client import Client

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = Client(intents=intents, command_prefix=' ', owner_id=475354677773336596)

    @client.tree.command(name="ping", description="Get the client latency.", guild=const.GUILD)
    async def ping(interaction: discord.Interaction):
        return await interaction.response.send_message(f"{(client.latency * 1000):.3f}ms", ephemeral=True)

    client.run(const.APP_TOKEN)