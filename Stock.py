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
            realTime = Helpers(item['symbol'])


            current_equity = float(item['quantity']) * float(realTime.currentPrices()['ask_price'])
            price_paid = float(item['quantity']) * float(item['average_buy_price'])

            # include rule object for the holding return statment
                # the rules be will sent through an api or a form from the frontend
                # each symbol will have it's own set of rules OPTIONS will be in Options.py

            hold = {
            "symbol": item['symbol'],
            "average_buy_price": item['average_buy_price'],
            "quantity": item['quantity'],
            "price_paid": price_paid,
            "current_equity": current_equity,
            "current_price": realTime.currentPrices(),
            "profit": round(float(current_equity) - float(price_paid), 2)
            }

            holdings.append(hold)
            
        return holdings


# USE THIS FOR TESTING
# def login():
#     login = r.login(email, password)

# login()
# tester = Stock()
# tester.get_current_positions()