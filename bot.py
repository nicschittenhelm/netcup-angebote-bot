import discord
from discord.ext import commands, tasks
from secrets import BOT_TOKEN

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(client.user.name)

@client.command(aliases=[""])
async def embed(ctx):
    embed = discord.Embed(title = 'VPS QWERTZ', description = 'vServer / Root-Server')
    embed.add_field(name = "NUR 7,98 EUR / Monat.", value = '[Direkt zum angebot](https://www.netcup-sonderangebote.de/vserver/vps-quertz/)')
    embed.set_thumbnail(url = 'https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/fd/fe/bc/fdfebc9b-e1f8-732d-faad-c0fc2a608bf7/source/512x512bb.jpg')
    await ctx.send(embed=embed)

@tasks.loop(seconds=5)
async def loop():
    print('Klappt!')

loop.start()



client.run(BOT_TOKEN)