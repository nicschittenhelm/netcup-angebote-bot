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
            embed.add_field(name = '!netcup hier', value = 'Legt Channel fest in welchem Angebote gepostet werden', inline = True)
            embed.add_field(name = '!netcup intervall', value = 'Legt den Intervall fest in welchem nach Updates gesucht wird. (Standardwert ist 15 Minuten)', inline = True)
            embed.add_field(name = '\u200B', value ='\u200B', inline = False)
            embed.set_footer(text = 'https://github.com/ebrofi/netcup-angebote-bot', icon_url = 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png')
            await ctx.send(embed=embed)

    if args[0] == 'gutscheine':
        embed = discord.Embed(
            title = 'Gutscheine',
            description = 'Codes können [hier](https://www.netcup.de/bestellen/gutschein_einloesen.php) eingelöst werden. Hierbei handelt es sich um Gutscheine aus dem Netcup Partnerprogramm und unterstützen den Entwickler',
            color = discord.Color.from_rgb(4,100,116)
            )
        embed.add_field(name = '5€ Gutschein (für Neukunden, keine Domains)', value = '36nc16446083830', inline = True)
        embed.add_field(name = 'Webhosting 2000 30% Rabatt', value = '1927nc16446083870	', inline = True)
        embed.add_field(name = 'Webhosting 4000 30% Rabatt', value = '1928nc16446083930	', inline = True)
        embed.add_field(name = 'Webhosting 8000 30% Rabatt', value = '1929nc16446083950	', inline = True)
        embed.add_field(name = 'VPS 200 G8 10% Rabatt', value = '2052nc16446083970', inline = True)
        embed.add_field(name = 'VPS 500 G8 10% Rabatt', value = '2053nc16446084000	', inline = True)
        embed.add_field(name = 'VPS 1000 G8 10% Rabatt', value = '2054nc16446084030	', inline = True)
        embed.add_field(name = 'VPS 2000 G8 10% Rabatt', value = '2056nc16446084060', inline = True)
        embed.add_field(name = 'RS 1000 SSD G7SE 30% Rabatt', value = '2057nc16446084080', inline = True)
        embed.add_field(name = 'RS 1000 SAS G8 30% Rabatt', value = '2201nc16446084110', inline = True)
        embed.add_field(name = 'RS 1000 SSD G8 30% Rabatt', value = '2202nc16446084130', inline = True)
        embed.add_field(name = 'Webhosting 2000 SE 30% Rabatt', value = '2234nc16446084160', inline = True)
        embed.add_field(name = 'Webhosting 4000 SE 30% Rabatt', value = '2235nc16446084180', inline = True)
        embed.add_field(name = 'Webhosting 8000 SE 30% Rabatt', value = '2236nc16446084210', inline = True)
        embed.add_field(name = 'VPS 1000 G9 1M Rabatt', value = '2609nc16446084240', inline = True)
        embed.add_field(name = 'VPS 2000 G9 1M Rabatt', value = '2610nc16446084260', inline = True)
        embed.add_field(name = 'VPS 3000 G9 1M Rabatt', value = '2611nc16446084290', inline = True)
        embed.add_field(name = 'VPS 4000 G9 1M Rabatt', value = '2612nc16446084310', inline = True)
        embed.add_field(name = 'VPS 6000 G9 1M Rabatt', value = '2613nc16446084340', inline = True)
        embed.add_field(name = 'VPS 8000 G9 1M Rabatt', value = '2614nc16446084390', inline = True)
        embed.add_field(name = 'RS 1000 G9 3M Rabatt', value = '2716nc16446084430', inline = True)
        embed.add_field(name = 'RS 2000 G9 3M Rabatt', value = '2717nc16446084460', inline = True)
        embed.add_field(name = 'RS 4000 G9 2M Rabatt', value = '2718nc16446084490', inline = True)
        embed.add_field(name = 'RS 8000 G9 1M Rabatt', value = '2719nc16446084540', inline = True)
        embed.set_footer(text = 'https://github.com/ebrofi/netcup-angebote-bot', icon_url = 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png')
        await ctx.send(embed=embed)

    if args[0] == 'hier':
        channel_id = ctx.channel.id
        await ctx.send('Updates werden ab jetzt hier gepostet.')
    
    if args[0] == 'intervall':
        loop.change_interval(minutes=float(args[1]))
        await ctx.send('Der Updateintervall wurde auf %s Minuten gesetzt' % args[1])

@tasks.loop(minutes=1)
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