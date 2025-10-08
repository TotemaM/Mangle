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
import discord
import os

# Launching program with "production" as second parameter, will run the production discord bot.
# Anything else launches the development bot.
import sys

if len(sys.argv) == 2 and sys.argv[1] == "production":
    GUILD = discord.Object(id=os.getenv("PROD_GUILD"))
    APP_TOKEN = os.getenv("PROD_APP_TOKEN")
else:
    GUILD = discord.Object(id=os.getenv("DEV_GUILD"))
    APP_TOKEN = os.getenv("DEV_APP_TOKEN")