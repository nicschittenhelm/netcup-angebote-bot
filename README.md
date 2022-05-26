# Netcup Angebote Bot

This is a quick and dirty implementation of a Discord bot posting the latest special offers from netcup.de/netcup.eu.

## Commands

- **!netcup help** Lists available commands.
- **!netcup hier** Tells the bot in which channel to post notifications.
- **!netcup intervall [minutes]** Lets you change the interval the bot checks for updates. (default is 15min)
- **!netcup gutscheine** Lists all available codes from the netcup affiliate program.

## Setup

###### This requires already having a bot created in the [Discord developer portal](https://discord.com/developers/applications).

1. Clone this repository to your debian based server. (make sure python and screen are installed)
1. Create a file called `secrets.py` in the same directory and add the following line: `BOT_TOKEN = 'your bot token here'`
1. Create new a new screen: `screen -S netcup-bot`
1. Inside the screen run the bot using: `python bot.py`

To make sure the bot is working, type `!netcup hier` in the channel you want the notification to be posted.
