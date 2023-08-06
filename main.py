from dotenv import load_dotenv
load_dotenv()
import os
from discord.ext import commands
import asyncio
token = os.getenv("TOKEN")
bumper_id = os.getenv("REMINDER_ID")
p = os.getenv("PREFIX") # add prefix to env 

bot = commands.Bot(help_command=None,max_messages=5,prefix=p) #use ext.commands instead of client


async def bump_loop(command,ctx):
    while True:
        await command(ctx)
        asyncio.sleep(7201) # pretty sure you can only bump once every 2 hours; time.sleep() will close the websocket connection

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')

@bot.event
async def on_message(message):
    if message.author.id == int(bumper_id): #doesn't let other people use it besides bumper, if you are running the command on that account, you can just add self_bot=True and remove this handler
        await bot.process_commands(message)

@bot.command()
async def bump(ctx):
    c = ctx.channel
    async for command in ctx.channel.slash_commands():
        if command.name == "bump":
            asyncio.create_task(bump_loop(command, ctx.channel)) #run on seperate thread 


bot.run(token)
