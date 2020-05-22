from argparse import ArgumentParser
from stocks import Stocks
from helpers import Helpers
from Watchlist import Watchlist
import robin_stocks as r



# THis is where the script will get the user credentials
parser = ArgumentParser(description="You will include the email and password to login to this")
email = parser.add_argument("-e", "--email",
                            action="store_true", dest="rank", default=False,
                            help="This is where you will include your email ")
password = parser.add_argument("-p", "--password",
                            action="store_true", dest="rank", default=False,
                            help="This is where you will include your password")


def login():
    login = r.login(email, password)

    return login['access_token']


if __name__ == "__main__":

    # IN ORDER TO DO ANYTHING, WE NEED TO LOGIN TO OUR ROBINHOOD ACCOUNT
    ##################################
    login()
    ##################################

    """
        Right here we are going feed the stock model our 
        - Technical data
        - Fundemental data
        - Level 1 data 
    """
    ##################################
    watchlist = Watchlist()
    stocks = Stocks(watchlist)
    ##################################

    # RETURN A LIST OF WHAT YOU OWN IN YOUR ROBINHOOD ACCOUNT
    ##################################
    stocks.get_owned_stocks()
    ##################################
    

