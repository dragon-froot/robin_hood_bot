import robin_stocks as r
import datetime
from helpers import Helpers 


class Stocks:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.currentDay = datetime.datetime.today().weekday()
        
    def login(self):
        email = self.email
        password = self.password

        login = r.login(email, password)
        #return the token
        return login['access_token']

    

    def get_owned_stocks(self):
        data = r.get_current_positions()

        for item in data:
            item['symbol'] = r.get_symbol_by_url(item['instrument'])
            
            realTime = Helpers(item['symbol'])

            
            total_spent = float(item['average_buy_price']) * float(item['quantity'])
            total_equity = float(item['quantity']) * float(realTime.currentPrices()['previous_close'])

            # Change return data based off of time and day
            if self.currentDay == 5 or 6:
                #This needs to change later to return a new object
                print('It is a weekend')

            holdings = {
                "average_buy_price": item['average_buy_price'],
                "symbol": item['symbol'],
                "quantity": item['quantity'],
                "current_price": realTime.currentPrices(),
                "total_spent": total_spent,
                "total_equity": total_equity 
            }
            print(holdings)
            

