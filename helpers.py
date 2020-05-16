import robin_stocks as r

class Helpers:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def currentPrices(self):
        symbol = self.symbol
        data = r.get_quotes(symbol)

        for item in data:
            return item