import robin_stocks as r

class Options:
    def __init__(self, watchlist):
        self.watchlist = watchlist

    def ironCondor(self):
        params = []
        for i in params:
            #if the watchlist meets params
            
            #1.) buy a call right above stayBelow
            #2.) sell a call at stayBelow

            #3.) buy a put right above stayAbove
            #4.) sell a pyt at stayAbove
