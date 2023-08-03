from dotenv import load_dotenv
load_dotenv()
import os
import time
import random
import discord
token = os.getenv("TOKEN")
bumper_id = os.getenv("REMINDER_ID")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # Only respond to the bumper reminder only if the pre-set reminder message is just a mention of our selfbot
        if message.author.id == int(bumper_id) and message.content == '<@1136503250749767730>':
            channel = client.get_channel(message.channel.id)
            async for command in channel.slash_commands():
                if command.name == "bump":
                    # Sleep for a random amount of time between 2 and 5 minutes not to look too suspicious
                    time.sleep(random.randint(120, 300))
                    await command(channel)

client = MyClient()
client.run(token)