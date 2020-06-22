from argparse import ArgumentParser
from Stock import Stock
from StockBot import StockBot
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
option = parser.add_argument("-o", "--options",
                              action="store_true", dest="rank", default=False,
                              help="Include this if you would like to sell options")


def login():
    login = r.login()

    return login['access_token']


if __name__ == "__main__":
#------------#
    login()
#------------#

#        GLOBAL
#------------------------------#
h = datetime.now().hour
m = datetime.now().minute
# The following line bugs out for some reason. It was 022
# current_time = eval(f"{h}{m}")
current_holdings = Stock().get_current_positions()
#------------------------------#



        # print(item)

# This will run between 6:30am and 3:32pm
# while current_time >= int(628) and current_time < int(1530):

while True:
    print(current_holdings)

    time.sleep(4)
    
    

    
    

