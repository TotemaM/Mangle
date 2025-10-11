################################################################################
#                                            __  __                   _        #
# const.py                                  |  \/  |                 | |       #
#                                           | \  / | __ _ _ __   __ _| | ___   #
# MICHELETTI Matteo                         | |\/| |/ _` | '_ \ / _` | |/ _ \  #
# (https://github.com/TotemaM)              | |  | | (_| | | | | (_| | |  __/  #
#                                           |_|  |_|\__,_|_| |_|\__, |_|\___|  #
# This file is under MIT licence                                 __/ |         #
#                                                               |___/          #
################################################################################

import dotenv
dotenv.load_dotenv()
import os

# Launching program with "production" as second parameter, will run the production discord bot.
# Anything else launches the development bot.
import sys

if len(sys.argv) == 2 and sys.argv[1] == "production":
    APP_TOKEN = os.getenv("PROD_APP_TOKEN")
    GUILD_ID = 1246471994195705876
    BOT_CHANNEL_ID = 1426683358414639215

else:
    APP_TOKEN = os.getenv("DEV_APP_TOKEN")
    GUILD_ID = 1423408793089347596
    BOT_CHANNEL_ID = 1424043802762412182

if not APP_TOKEN:
    print("Missing .env variable(s)")
    exit(1)