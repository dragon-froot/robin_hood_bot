import robin_stocks as r 
import datetime
import time


class Bot:
    def __init__(self, watchlist, current_positions, trade_indicators):
        self.watchlist = watchlist
        self.current_positions = current_positions
        self.trade_indicators = current_positions
    
    def check_current_positions_for_change(self):
        current_positions = self.current_positions
        
        for item in current_positions:
            symbol = item['symbol']
            total_equity = item['total_equity']
            current_price = item['current_price']['last_trade_price']

            current_value = float(item['quantity']) * float(current_price)

            change = {
                "symbol": symbol,
                "total_equity": total_equity,
                "profit": round(float(current_value) - float(total_equity), 2)
                # "current_price": item['current_price']
            }

            print(change)


