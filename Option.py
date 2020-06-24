import robin_stocks as r
import time


class Option:
    
    def get_current_options(self):
        orders = r.get_all_option_orders()
        return orders



r.login()

options = Option().get_current_options()

print(options)



#  {
#       "cancel_url":"None",
#       "canceled_quantity":"1.00000",
#       "created_at":"2020-06-23T19:38:44.097430Z",
#       "direction":"credit",
#       "id":"cf985959-7cd4-4910-b442-8b90c3b61ed1",
#       "legs":[
#          {
#             "executions":[

#             ],
#             "id":"c3cf4d82-e5f6-4727-a0bf-696beac4be37",
#             "option":"https://api.robinhood.com/options/instruments/5cd328b2-012c-4fb1-845b-2068d47dcad5/",
#             "position_effect":"close",
#             "ratio_quantity":1,
#             "side":"sell"
#          }
#       ],
#       "pending_quantity":"0.00000",
#       "premium":"9.00000000",
#       "processed_premium":"0.0000",
#       "price":"0.09000000",
#       "processed_quantity":"0.00000",
#       "quantity":"1.00000",
#       "ref_id":"375750C7-9087-4F55-BB21-CFB505DAC3AB",
#       "state":"cancelled",
#       "time_in_force":"gfd",
#       "trigger":"immediate",
#       "type":"limit",
#       "updated_at":"2020-06-23T20:37:32.892725Z",
#       "chain_id":"55d7e31c-9105-488b-983c-93e09dd7ff35",
#       "chain_symbol":"BAC",
#       "response_category":"end_of_day",
#       "opening_strategy":"None",
#       "closing_strategy":"long_call",
#       "stop_price":"None"
#    },