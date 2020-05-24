import robin_stocks as r 


class Watchlist:
    
    def get_current_watchlist(self):
        watchlist = r.get_watchlist_by_name(name="Default")
        fullList = list()
        for item in watchlist:
            watching = r.get_symbol_by_url(item['instrument'])

            fullList.append(watching)

        return fullList


            