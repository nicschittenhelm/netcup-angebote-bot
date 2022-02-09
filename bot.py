import discord
from discord.ext import commands, tasks
from secrets import BOT_TOKEN
from scraper import RunScraper

client = commands.Bot(command_prefix="!netcup")
channel_id = 938856334412095499

@client.event
async def on_ready():
    print(client.user.name)
    await client.get_channel(channel_id).send('Bot beigetreten!')

@client.command
async def here(ctx):
    await ctx.send('test')

@tasks.loop(seconds=5)
async def loop():
    await client.wait_until_ready()
    channel = client.get_channel(channel_id)
    print('Scraping starting...')
    # instantiate Scraper
    Scraper = RunScraper()

    if Scraper.check_update():
        print('NEUES ANGEBOT')
        for item in Scraper.whats_new():
            data = Scraper.build_data(item)
            print(data)
            embed = discord.Embed(title = data['title'], description = data['type'])
            embed.add_field(name = data['price'], value = '[Direkt zum Angebot](%s)' % data['link'])
            embed.set_thumbnail(url = 'https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/fd/fe/bc/fdfebc9b-e1f8-732d-faad-c0fc2a608bf7/source/512x512bb.jpg')
            await channel.send(embed=embed)

    # delete current instance of Scraper
    del Scraper


loop.start()

client.run(BOT_TOKEN)








# @client.command(aliases=["embed"])
# async def embed(ctx):
#     embed = discord.Embed(title = 'VPS QWERTZ', description = 'vServer / Root-Server')
#     embed.add_field(name = "NUR 7,98 EUR / Monat.", value = '[Direkt zum angebot](https://www.netcup-sonderangebote.de/vserver/vps-quertz/)')
#     embed.set_thumbnail(url = 'https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/fd/fe/bc/fdfebc9b-e1f8-732d-faad-c0fc2a608bf7/source/512x512bb.jpg')
#     await ctx.send(embed=embed)