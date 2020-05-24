import robin_stocks as r
from helpers import Helpers

class Stock:
    # def __init__(self):
    #     pass

    def get_current_positions(self):
        data = r.get_open_stock_positions()

        holdings = list()
        for item in data:
            item['symbol'] = r.get_symbol_by_url(item['instrument'])
            # Returns current_price object for a give symbol
            realTime = Helpers(item['symbol'])


            total_spent = float(item['average_buy_price']) * float(item['quantity'])
            total_equity = float(item['quantity']) * float(realTime.currentPrices()['last_trade_price'])

            hold = {
            "symbol": item['symbol'],
            "average_buy_price": item['average_buy_price'],
            "quantity": item['quantity'],
            "total_spent": total_spent,
            "total_equity": total_equity,
            "current_price": realTime.currentPrices(),
            # "profit": profit
            }

            holdings.append(hold)
            # return holdings
            # print(holdings)
        return holdings


# USE THIS FOR TESTING
# def login():
#     login = r.login(email, password)

# login()
# tester = Stock()
# tester.get_current_positions()