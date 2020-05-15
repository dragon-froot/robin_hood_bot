import requests 
import json
import robin_stocks as r
import sys


# While the program is running this makes sure that the user is logged in.
# Returns the access token as a string
def login():
    login = r.login('dragon-froot710@protonmail.com', '1185949Bobsaget1')
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
        print(holding)

def getCurrentPrices(sym):
    for i in sym:
        return i['price']
        
        


        

    
 
# login()
# get_list_of_owned_stocks()
hold = ['GOOGL', 'WORK']
if __name__ == "__main__":
    
    login()
    owned_stocks()

        # hold will be the return value of owned_stocks
        


# Make sure that the user logs in from the terminal
# Have the owned_stocks return a list of our current holdings for the inverstopia api
