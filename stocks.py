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
        

        
        marker = 0
        for item in data:
            item['symbol'] = r.get_symbol_by_url(item['instrument'])
            marker = marker + 1
            realTime = Helpers(item['symbol'])

            
            total_spent = float(item['average_buy_price']) * float(item['quantity'])
            total_equity = float(item['quantity']) * float(realTime.currentPrices()['last_trade_price'])

            holdings = {
                "_id": marker,
                "symbol": item['symbol'],
                "average_buy_price": item['average_buy_price'],
                "quantity": item['quantity'],
                "total_spent": total_spent,
                "total_equity": total_equity,
                "current_price": realTime.currentPrices(),
                # "profit": profit
              
            }

            
            print(holdings)
            

