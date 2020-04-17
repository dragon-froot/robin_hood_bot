import requests 
import json
import robin_stocks as r 

# Returns the access token as a string
def login():
    login = r.login('dragon-froot710@protonmail.com', '1185949Bobsaget1')
    return login['access_token']

# Gets a list of all the stocks you own and returns an array of url's to get other data 
def get_list_of_owned_stocks():
    data = r.account.get_current_positions(info=None)
    for i in data:
        url = i['url']
        head = {'Accept': 'json', 'Authorizaton': 'Token ' + login()}
        res = requests.get(url, headers=head)
        print(res)

    # print(data)
 
login()
get_list_of_owned_stocks()
# print(login())



# get_list_of_owned_stocks info
# [
# {
#  'url': 'https://api.robinhood.com/positions/5UY31279/6df56bd0-0bf2-44ab-8875-f94fd8526942/',
#  'instrument': 'https://api.robinhood.com/instruments/6df56bd0-0bf2-44ab-8875-f94fd8526942/',
#  'account': 'https://api.robinhood.com/accounts/5UY31279/',
#  'account_number': '5UY31279',
#  'average_buy_price': '5.8500',
#  'pending_average_buy_price': '5.8500',
#  'quantity': '1.00000000',
#  'intraday_average_buy_price': '0.0000',
#  'intraday_quantity': '0.00000000',
#  'shares_held_for_buys': '0.00000000',
#  'shares_held_for_sells': '0.00000000',
#  'shares_held_for_stock_grants': '0.00000000',
#  'shares_held_for_options_collateral': '0.00000000',
#  'shares_held_for_options_events': '0.00000000',
#  'shares_pending_from_options_events': '0.00000000',
#  'updated_at': '2020-03-25T17:20:54.228055Z',
#  'created_at': '2020-03-12T15:23:03.516338Z'
# },
#  {
#   'url': 'https://api.robinhood.com/positions/5UY31279/0dd811b3-7047-448d-96e0-7bf6ee4cfe45/',
#   'instrument': 'https://api.robinhood.com/instruments/0dd811b3-7047-448d-96e0-7bf6ee4cfe45/',
#   'account': 'https://api.robinhood.com/accounts/5UY31279/',
#   'account_number': '5UY31279',
#   'average_buy_price': '21.6217',
#   'pending_average_buy_price': '21.6217', 'quantity': '6.00000000',
#   'intraday_average_buy_price': '0.0000',
#   'intraday_quantity': '0.00000000', 'shares_held_for_buys': '0.00000000',
#  'shares_held_for_sells': '0.00000000', 'shares_held_for_stock_grants': '0.00000000',
#  'shares_held_for_options_collateral': '0.00000000', 'shares_held_for_options_events': '0.00000000',
#  'shares_pending_from_options_events': '0.00000000', 'updated_at': '2020-03-24T16:34:07.088991Z', 'created_at': '2020-03-13T12:02:34.925686Z'
# },
#  {'url': 'https://api.robinhood.com/positions/5UY31279/71d81e7d-783c-4b8c-b574-ee50fcc4ce3a/', 'instrument': 'https://api.robinhood.com/instruments/71d81e7d-783c-4b8c-b574-ee50fcc4ce3a/', 'account': 'https://api.robinhood.com/accounts/5UY31279/', 'account_number': '5UY31279', 'average_buy_price': '0.7700', 'pending_average_buy_price': '0.7700', 'quantity': '34.00000000', 'intraday_average_buy_price': '0.6748', 'intraday_quantity': '23.00000000', 'shares_held_for_buys': '0.00000000', 'shares_held_for_sells': '0.00000000', 'shares_held_for_stock_grants': '0.00000000', 'shares_held_for_options_collateral': '0.00000000', 'shares_held_for_options_events': '0.00000000', 'shares_pending_from_options_events': '0.00000000', 'updated_at': '2020-04-16T14:41:49.862926Z', 'created_at': '2020-03-13T15:19:07.106024Z'
# }, {'url': 'https://api.robinhood.com/positions/5UY31279/3324b13c-dc23-40e8-8807-76d87fdb09ed/', 'instrument': 'https://api.robinhood.com/instruments/3324b13c-dc23-40e8-8807-76d87fdb09ed/', 'account': 'https://api.robinhood.com/accounts/5UY31279/', 'account_number': '5UY31279', 'average_buy_price': '15.8400', 'pending_average_buy_price': '15.8400', 'quantity': '3.00000000', 'intraday_average_buy_price': '0.0000', 'intraday_quantity': '0.00000000', 'shares_held_for_buys': '0.00000000', 'shares_held_for_sells': '0.00000000', 'shares_held_for_stock_grants': '0.00000000', 'shares_held_for_options_collateral': '0.00000000', 'shares_held_for_options_events': '0.00000000', 'shares_pending_from_options_events': '0.00000000', 'updated_at': '2020-03-25T17:20:26.562758Z', 'created_at': '2020-03-25T17:19:40.033439Z'
# }, {'url': 'https://api.robinhood.com/positions/5UY31279/995cc73e-63d8-4081-8937-8320460d4ef0/', 'instrument': 'https://api.robinhood.com/instruments/995cc73e-63d8-4081-8937-8320460d4ef0/', 'account': 'https://api.robinhood.com/accounts/5UY31279/', 'account_number': '5UY31279', 'average_buy_price': '2.8400', 'pending_average_buy_price': '2.8400', 'quantity': '20.00000000', 'intraday_average_buy_price': '2.8400', 'intraday_quantity': '20.00000000', 'shares_held_for_buys': '0.00000000', 'shares_held_for_sells': '0.00000000', 'shares_held_for_stock_grants': '0.00000000', 'shares_held_for_options_collateral': '0.00000000', 'shares_held_for_options_events': '0.00000000', 'shares_pending_from_options_events': '0.00000000', 'updated_at': '2020-04-16T14:40:24.554638Z', 'created_at': '2020-04-16T04:03:27.051682Z'}
# ]
