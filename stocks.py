import datetime
from helpers import Helpers 
# import robin_stocks as r
import robin_stocks as r

class Stocks:
    def __init__(self, watchlsist):
        self.watchlsist = watchlsist
        self.currentDay = datetime.datetime.today().weekday()
        
    


    def get_owned_stocks(self):
        # data = r.get_current_positions()
        data = r.get_all_positions()
        

        
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
            

