import os
import requests
import discord
from discord import app_commands

BotToken = "yourbottoken"
yoururl = "url/update"

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
            print("Synced Commands")
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="https://github.com/xxpwnxxx420lord"
            )
        )
        print('working <3')

    async def on_close(self):
        print("Bot is shutting down...")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name="kickplayer", description="Kicks a player if found")
async def kickplayer(interaction: discord.Interaction, user: str):
    response = requests.post(yoururl, json={"content": user})
    
    if response.status_code == 200:
        await interaction.response.send_message(f"Sent request to kick {user}")
    else:
        await interaction.response.send_message(f"Failed to send request. Status: {response.status_code}")

try:
    client.run(BotToken)
except Exception as e:
    print(f"An error occurred: {e}")
