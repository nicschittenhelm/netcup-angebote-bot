import discord
from discord.ext import commands, tasks
from secrets import BOT_TOKEN
from scraper import RunScraper

bot = commands.Bot(command_prefix='!')
channel_id = int()
first_start = True

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print('Bot ist bereit!')

@bot.command()
async def netcup(ctx, *args):
    await bot.wait_until_ready()
    global channel_id

    if args[0] == 'help':
            embed = discord.Embed(
                title = 'Hilfestellung',
                description = 'Bei Problemen ein Github [Issue](https://github.com/ebrofi/netcup-angebote-bot/issues) erstellen',
                color = discord.Color.from_rgb(4,100,116)
                )
            embed.add_field(name = '\u200B', value ='\u200B', inline = False)
            embed.add_field(name = '!netcup here', value = 'Legt Channel fest in welchem Angebote gepostet werden', inline = True)
            embed.add_field(name = '!netcup intervall', value = 'Legt den Intervall fest in welchem nach Updates gesucht wird. (Standardwert ist 15 Minuten)', inline = True)
            embed.add_field(name = '\u200B', value ='\u200B', inline = False)
            embed.set_footer(text = 'https://github.com/ebrofi/netcup-angebote-bot', icon_url = 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png')
            await ctx.send(embed=embed)

    if args[0] == 'here':
        channel_id = ctx.channel.id
        await ctx.send('Updates werden ab jetzt hier gepostet.')
    
    if args[0] == 'intervall':
        loop.change_interval(minutes=float(args[1]))
        await ctx.send('Der Updateintervall wurde auf %s Minuten gesetzt' % args[1])

@tasks.loop(minutes=15)
async def loop():
    global first_start
    await bot.wait_until_ready()
    channel = bot.get_channel(channel_id)
    print('Scraping starting...')
    # instantiate Scraper
    Scraper = RunScraper()

    if Scraper.check_update():
        print('NEUES ANGEBOT')
        for item in Scraper.whats_new():
            if not first_start:
                data = Scraper.build_data(item)
                print(data)
                embed = discord.Embed(title = data['title'], description = data['type'], color = discord.Color.from_rgb(4,100,116))
                embed.add_field(name = data['price'], value = '[Direkt zum Angebot](%s)' % data['link'])
                embed.set_thumbnail(url = 'https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/fd/fe/bc/fdfebc9b-e1f8-732d-faad-c0fc2a608bf7/source/512x512bb.jpg')
                await channel.send(embed=embed)

    # delete current instance of Scraper
    del Scraper
    first_start = False


loop.start()

bot.run(BOT_TOKEN)








# @bot.command(aliases=['embed'])
# async def embed(ctx):
#     embed = discord.Embed(title = 'VPS QWERTZ', description = 'vServer / Root-Server')
#     embed.add_field(name = 'NUR 7,98 EUR / Monat.', value = '[Direkt zum angebot](https://www.netcup-sonderangebote.de/vserver/vps-quertz/)')
#     embed.set_thumbnail(url = 'https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/fd/fe/bc/fdfebc9b-e1f8-732d-faad-c0fc2a608bf7/source/512x512bb.jpg')
#     await ctx.send(embed=embed)