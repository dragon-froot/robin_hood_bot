from argparse import ArgumentParser
import robin_stocks as r
import time
from datetime import datetime
# Class Imports
from Stock import Stock
from Option import Option
from Portfolio import Portfolio


# THis is where the script will get the user credentials
parser = ArgumentParser(description="You will include the email and password to login to this")

email = parser.add_argument("-e", "--email", action="store_true", dest="rank", default=False, help="This is where you will include your email ")
password = parser.add_argument("-p", "--password", action="store_true", dest="rank", default=False, help="This is where you will include your password")



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
# current_time = eval(f"{h}{m}") #IDK why this line isn't working
currentHoldings = Stock().get_current_positions()
currentOptions = Option().get_current_options()
portfolio = Portfolio(currentHoldings).portfolio_worth()
#------------------------------#



# This will run between 6:30am and 3:32pm
# while current_time >= int(628) and current_time < int(1530):

# print(portfolio)
        

    
    
time.sleep(2)
    
    

    
    

