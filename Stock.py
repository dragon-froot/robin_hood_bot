import robin_stocks as r
from helpers import Helpers
#consider adding a class that given x as holdings, rules? 


class Stock:
    
    def get_current_positions(self):
        data = r.get_open_stock_positions()

        holdings = list()
        for item in data:
            item['symbol'] = r.get_symbol_by_url(item['instrument'])

            # Returns current_price object for a give symbol
            helperFunction = Helpers(item['symbol'])
            currentData = helperFunction.currentPrices()

            current_equity = float(item['quantity']) * float(currentData['ask_price'])
            price_paid = float(item['quantity']) * float(item['average_buy_price'])
            
            singleHolding = {
                "symbol": item['symbol'],
                "quantity": item['quantity'],
                "current_price": currentData['ask_price'],
                "average_buy_price": item['average_buy_price'],
                "price_paid": price_paid,
                "current_equity": current_equity,
                "profit": round(float(current_equity) - float(price_paid), 2)
            }

            holdings.append(singleHolding)
            
        return holdings


