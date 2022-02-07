import discord
from discord.ext import commands, tasks
from secrets import BOT_TOKEN
from scraper import update

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(client.user.name)

# @client.command(aliases=["embed"])
# async def embed(ctx):
#     embed = discord.Embed(title = 'VPS QWERTZ', description = 'vServer / Root-Server')
#     embed.add_field(name = "NUR 7,98 EUR / Monat.", value = '[Direkt zum angebot](https://www.netcup-sonderangebote.de/vserver/vps-quertz/)')
#     embed.set_thumbnail(url = 'https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/fd/fe/bc/fdfebc9b-e1f8-732d-faad-c0fc2a608bf7/source/512x512bb.jpg')
#     await ctx.send(embed=embed)

# @client.command(aliases=["debugging"])
# async def update(ctx):
#     print('Klappt!')
#     print(check_update(items_new))



@tasks.loop(seconds=5)
async def loop():
    #print('Klappt!')
    update()

loop.start()

async def embed(ctx, title, type, price, link):
    embed = discord.Embed(title = title, description = type)
    embed.add_field(name = price, value = link)
    embed.set_thumbnail(url = 'https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/fd/fe/bc/fdfebc9b-e1f8-732d-faad-c0fc2a608bf7/source/512x512bb.jpg')
    await ctx.send(embed=embed)



client.run(BOT_TOKEN)