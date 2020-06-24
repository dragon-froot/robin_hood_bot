import robin_stocks as r
import time

class Portfolio:
    def __init__(self, stocks):
        self.stocks = stocks

    def portfolio_worth(self):
        stocks = self.stocks
        
        for item in stocks:
            return item['symbol']    
        
        
        