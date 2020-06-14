import time 
import robin_stocks as r
import sys

class Bot:
    def __init__(self, currentHolding, sellRules):
        self.currentHolding = currentHolding
        self.sellRules = sellRules
        

    def sellAtPercent(self):
        currentHolding = self.currentHolding

        pricePaid = currentHolding['price_paid']
        currentEquity = currentHolding['current_equity']

        


