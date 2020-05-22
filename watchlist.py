import robin_stocks as r
import time


def get_watchlist():
    data = r.get_watchlist_by_name(name="Default")
    watching = []

    for item in data:
        watch = r.get_symbol_by_url(item['instrument'])
        # This takes way too long to run
        watching.append(watch)

    print(watching)


# get_watchlist()