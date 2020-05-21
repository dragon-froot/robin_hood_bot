from argparse import ArgumentParser
from stocks import Stocks
from helpers import Helpers
from watchlist import get_watchlist

# THis is where the script will get the user credentials
parser = ArgumentParser(description="You will include the email and password to login to this")
email = parser.add_argument("-e", "--email",
                            action="store_true", dest="rank", default=False,
                            help="This is where you will include your email ")
password = parser.add_argument("-p", "--password",
                            action="store_true", dest="rank", default=False,
                            help="This is where you will include your password")





if __name__ == "__main__":
    watchlist = get_watchlist()

    stocks = Stocks(email, password)
    

    # LOGIN AND RETURN A LIST OF WHAT YOU OWN IN YOUR ROBINHOOD ACCOUNT
    ##############################################
    stocks.login()
    stocks.get_owned_stocks()
    #############################
    while True:
        pass

