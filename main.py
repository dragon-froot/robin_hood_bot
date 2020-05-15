import requests 
import json
import robin_stocks as r
import sys
from argparse import ArgumentParser

# THis is where the script will get the user credentials
parser = ArgumentParser(description="You will include the email and password to login to this")
email = parser.add_argument("-e", "--email",
                            action="store_true", dest="rank", default=False,
                            help="This is where you will include your email ")
password = parser.add_argument("-p", "--password",
                            action="store_true", dest="rank", default=False,
                            help="This is where you will include your password")

# While the program is running this makes sure that the user is logged in.
# Returns the access token as a string
def login():
    # login = r.login('dragon-froot710@protonmail.com', '1185949Bobsaget1')
    login = r.login(email, password)
    return login['access_token']

    # print(login['access_token'])

# Gets a list of all the stocks you own and returns an array of url's to get other data 
def owned_stocks():
    data = r.get_current_positions()
    length = len(data)
    #returns a list of the symbols of my current holdings
    for item in data:
        item['symbol'] = r.get_symbol_by_url(item['instrument'])
        holding = {
            "price": item['average_buy_price'],
            "symbol": item['symbol']
        }
        getCurrentPrices(item['symbol'])




def getCurrentPrices(sym):
    req = requests.get('https://robinhood.com/stocks/{0}', sym)
    print(req.data)
        
        


        

    
 
# login()
# get_list_of_owned_stocks()
hold = ['GOOGL', 'WORK']
if __name__ == "__main__":
    
    login()
    owned_stocks()

        # hold will be the return value of owned_stocks
        


# Make sure that the user logs in from the terminal
# Have the owned_stocks return a list of our current holdings for the inverstopia api
