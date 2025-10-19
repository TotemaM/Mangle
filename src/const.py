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
    # Channels ID :
    BOT_CHANNEL_ID = 1426683358414639215
    REQUEST_CHANNEL_ID = 1426999839312449647
    LOG_CHANNEL_ID = 1429491265787133972
    # Roles ID :
    BDE_NOTIFY_ROLE_ID = 1426986632661172255
    # Unlogged categories ("Information", "Discord admin" and "Admin") :
    NOT_LOGGED_CATEGORIES_IDS = [1246471994195705877, 1426161950613573792, 1246480079585018038]
else:
    APP_TOKEN = os.getenv("DEV_APP_TOKEN")
    GUILD_ID = 1423408793089347596
    # Channels ID :
    BOT_CHANNEL_ID = 1424043802762412182
    REQUEST_CHANNEL_ID = 1426903689846849590
    LOG_CHANNEL_ID = 1429497328519086101
    # Roles ID :
    BDE_NOTIFY_ROLE_ID = 1423410272940326942
    # Unlogged categories ("Information", "Discord admin" and "Admin") :
    NOT_LOGGED_CATEGORIES_IDS = [1423623754113744956, 1425610232251547718, 1423410525768777798]

if not APP_TOKEN:
    print("Missing .env variable(s)")
    exit(1)