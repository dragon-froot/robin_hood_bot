import robin_stocks as r
import time


class Option:
    def get_current_options(self):
        orders = r.get_open_option_positions()
        
        return orders

r.login()
options = Option().get_current_options()

print(options)

