import robin_stocks as r 


class Watchlist:
    def get_current_watchlist():
        watchlist = r.get_watchlist_by_name(name="Default")
        fullList = list()
        for item in watchlist:
            watching = r.get_symbol_by_url(item['instrument'])

            full_list.append(watching)

        return fullList


            