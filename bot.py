import discord
from secrets import BOT_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)








client.run(BOT_TOKEN)