from argparse import ArgumentParser
from Stock import Stock
from helpers import Helpers
from Watchlist import Watchlist
from Bot import Bot
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
    login()

    watchlist = Watchlist()
    current_positions = Stock()
    bot = Bot(watchlist.get_current_watchlist(),
              current_positions.get_current_positions(),
             "Tester")

    bot.check_current_positions_for_change()


    
    

