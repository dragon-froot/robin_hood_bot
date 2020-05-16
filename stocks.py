import robin_stocks as r
from helpers import Helpers 


class Stocks:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
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
            
            holdings = {
                "buy_price": item['average_buy_price'],
                "symbol": item['symbol'],
                "quantity": item['quantity'],
                "current_price": realTime.currentPrices()
            }
            print(holdings)

