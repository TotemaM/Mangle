# Mangle
Mangle is a Discord bot for the 42 Belgium BDE Discord server.

## Requirements
| Program | Version |
|---------|---------|
| Python  | 3.10.12 |
| PIP     | 24.3.1  |

To install the following PIP packages you can run `pip install -r requirements.txt`

| PIP Package   | Version |
|---------------|---------|
| python-dotenv | 1.1.1   |
| discord.py    | 2.6.3   |

## Deploy
You have to set given variables inside a `.env` file.
```
PROD_APP_TOKEN=<Prod Discord app token>
PROD_APP_ID=<Prod Discord Bot ID>
PROD_GUILD=<Prod Discord bot guild ID>

DEV_APP_TOKEN=<Dev Discord app token>
DEV_APP_ID=<Dev Discord Bot ID>
DEV_GUILD=<Dev Discord bot guild ID>
```