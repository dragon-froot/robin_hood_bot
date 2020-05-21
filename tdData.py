import requests
import time
import datetime
from config import CONSUMER_KEY

def get_price_history(**kwargs):
    key = CONSUMER_KEY
    url = 'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(kwargs.get('symbol'))

    params = {}
    params.update({'apikey': key })

    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params.update(parameter)
    
    return requests.get(url, params=params).json()


def printTime():
    data = get_price_history(symbol="EXTR", period=1, periodType='day', frequencyType='minute')

    for item in data['candles']:
        # newTime = time.strftime("%D %H:%M", time.localtime(int(item['datetime'])))
        newTime = datetime.fromtimestamp(item['datetime']).strftime("%Y-%m-%d %H:%M:%S.%f")

        
        print(newTime)
        time.sleep(1)

def get_realtime_data():
    symbol = 'EXTR'
    url = 'https://api.tdameritrade.com/v1/marketdata/{}/quotes'.format(symbol)
    params = {}
    params.update({'apikey': CONSUMER_KEY})

    data = requests.get(url, params=params).json()
    print(data)

get_realtime_data()
# printTime()

