# Mangle
Mangle is a Discord bot for the 42 Belgium BDE Discord server.

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

| PIP Package   | Version  |
|---------------|----------|
| python-dotenv | 1.1.1    |
| nextcord      | 3.1.1    |

## Deploy
You have to set given variables inside a `.env` file.
```
PROD_APP_TOKEN=<Prod Discord app token>
DEV_APP_TOKEN=<Dev Discord app token>
```
To run the program with the production credentials you have to run it with 1 arg equals to `production`.  
Anything else will run it with the development credentials.

## Command list
### User
- `/create_voice_channel` : Allow a user to create his own voice channel. Auto deleted when everyone left.
- `/request_bde` : Make a request to the BDE staff.

### Administrator
- `/message` : Allows to send an embed message in the current text channel.
- `/message_edit` : Edit a previously send, embed message.
