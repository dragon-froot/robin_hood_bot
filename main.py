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
def login():
    
    login = r.login(email, password)
    #return the account access token for future requests
    return login['access_token']


# Gets a list of all the stocks you own and returns an array of url's to get other data 
def owned_stocks():
    data = r.get_current_positions()
    length = len(data)
    #returns a list of the symbols of my current holdings
    for item in data:
        item['symbol'] = r.get_symbol_by_url(item['instrument'])


        current = getCurrentPrices(item['symbol'])
        holding = {
            "buy_price": item['average_buy_price'],
            "symbol": item['symbol'],
            "quantity": item['average_buy_price'],
            "current_price": current['ask_price']
        }
        
        print(holding)




def getCurrentPrices(sym):
    data = r.get_quotes(sym)
    
    for i in data:
        return i
        
        



if __name__ == "__main__":
    
    login()
    owned_stocks()
    


