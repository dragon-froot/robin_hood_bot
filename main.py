from argparse import ArgumentParser
from Stock import Stock
from helpers import Helpers
from Watchlist import Watchlist
from Options import Options
from Bot import Bot
import robin_stocks as r

import time
from datetime import datetime


# THis is where the script will get the user credentials
parser = ArgumentParser(description="You will include the email and password to login to this")
email = parser.add_argument("-e", "--email",
                            action="store_true", dest="rank", default=False,
                            help="This is where you will include your email ")
password = parser.add_argument("-p", "--password",
                            action="store_true", dest="rank", default=False,
                            help="This is where you will include your password")


def login():
    login = r.login()

    return login['access_token']


if __name__ == "__main__":
#------------#
    login()
#------------#

h = datetime.now().hour
m = datetime.now().minute
current_time = eval(f"{h}{m}")

# This will run between 6:30am and 3:32pm
while current_time >= int(628) and current_time < int(1530):

    # Return []
    current_holdings = Stock().get_current_positions()

    print(current_time)

    def checkCurrentHoldings(current_holdings):
        for item in current_holdings:
            price = item['average_buy_price']


    
    time.sleep(10)

    
    

