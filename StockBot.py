import time 
import robin_stocks as r
import sys

class StockBot:
    def __init__(self, currentHoldings):
        self.currentHolding = currentHoldings
        
        
    def potentialSells(self):
        currentHoldings = self.currentHoldings
        holdings = list()
        for item in currentHoldings:
            currentEquity = item['currentEquity']
            pricePaid = item['price_paid']

            

        


