import robin_stocks as r

class Helpers:
    def __init__(self, symbol):
        self.symbol = symbol
        # self.watchlist = watchlist
    
    def currentPrices(self):
        symbol = self.symbol
        data = r.get_quotes(symbol)

        for item in data:
            return item
    
    # def checkWatchList(self, list):
    #     watchlist = self.watchlist

    #     for holding in watchlist:
    #         pass
"""
MovAvgExponential
https://tlc.thinkorswim.com/center/reference/Tech-Indicators/studies-library/M-N/MovAvgExponential.html
EMA1 = price1;

EMA2 = α*price2 + (1 - α)*EMA1;

EMA3 = α*price3 + (1 - α)*EMA2;

EMAN = α*priceN + (1 - α)*EMAN-1;

"""


