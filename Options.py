import robin_stocks as r 

class Options:
    def showOptions(self):
        positions = r.get_all_option_positions()

        for item in positions:
            print(item)