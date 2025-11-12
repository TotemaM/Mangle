# Mangle
Mangle is a Discord bot for the 42 Belgium student associations Discord server.

## Requirements
The following versions might not be necessary to make the script work.
They're just mentioned because well known to work

| Program | Version |
|---------|---------|
| Python  | 3.12    |
| PIP     | 24.3.1  |

To install the following PIP packages you can run
```
mkdir .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

| PIP Package   | Version |
|---------------|---------|
| python-dotenv | 1.1.1   |
| nextcord      | 3.1.1   |
| qrcode        | 8.2     |
| pillow        | 12.0.0  |

## Deploy
You have to set given variables inside a `.env` file.
```
PROD_APP_TOKEN=<Prod Discord app token>
DEV_APP_TOKEN=<Dev Discord app token>
```

### Constants
Inside the `const.py` file, you have to define some discord IDs
```
GUILD_ID: int

BOT_CHANNEL_ID: int
REQUEST_CHANNEL_ID: int
LOG_CHANNEL_ID: int

BDE_NOTIFY_ROLE_ID: int

NOT_LOGGED_CATEGORIES_IDS: List[int]
```

### Run
#### GNU Make
If you have GNU Make installed you can run `make` for dev or `make production` for prod execution.
#### Vanilla Python
Otherwise you can run the python script directly with following instructions :  
To run the program with the production credentials you have to run it with 1 arg equals to `production`.  
Anything else will run it with the development credentials.
```
python3 src/main.py
# or
python3 src/main.py production
```

## Functionalities
### Administrative
#### Bot messages
`/message` : You can use the bot to send messages of any type, default or embed.
`/message_edit` : Allow to edit a previously send message by the bot.
#### Event logger
The bot logs all following events into a channel :
- Message modified
- Message deleted
- Any internal error, for debugging purpose
- Any command tried, by any user.

It also deletes all the messages that are not commands. in the command channel.
#### QR Code generator
`/qr` : Command allowing to generate a QR code based on some parameters.
### User
#### Custom voice channels
`/create_voice_channel` : Command to allow users to generate their own voice channel.
#### Requesting the BDE Staff
`/request_bde`Ticket tool command, for club requests or anything else.
### Other Events
#### Guild icon
The guild icon changed based on calendar dates, for the following events :
- No event, default icon
- Halloween
