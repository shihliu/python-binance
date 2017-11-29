from binance.client import Client
import json
import time
import web
import thread
import urllib3
http = urllib3.poolmanager()
from datetime import datetime
client = Client('yq67cDjrCxGl6eeKMyTeiK1zkeArFpu8v4uB4b6TWDQdgjDlH0KjmXfHBZ1NjvJj', 'DxE7Wugo75EK8mLmybY76dbZW6tROpyNjBRd9NHsEOXqBaKq6Awgul4390xwRUdc')

# open_order = client.get_open_orders(symbol='QSPETH')

# order_book = client.get_order_book(symbol='QSPETH')
# print order_book
urls = (
    '/big_trade', 'index',
    )

def get_big_trade(strd_amount, strd_time):
    aggregate_all = client.get_aggregate_trades(symbol='QSPETH')
    all_buy_price = all_buy_amount= 0.0
    all_sell_price = all_sell_amount= 0.0
    strd_time = strd_time * 1000
    curr_serv_time = client.get_server_time()["serverTime"]
    print "curr_serv_time is %s" %curr_serv_time
    
    for i in aggregate_all:
        dela_time = curr_serv_time - i['T']
    #     print "current trade time is %s" %i['T']
    #     print "dela_time is %s" %dela_time
        if dela_time < strd_time:
            if i["m"] is True:
                all_buy_price = all_buy_price + float(i["p"]) * float(i["q"])
                all_buy_amount = all_buy_amount + float(i["q"])
                if float(i["q"]) > strd_amount:
                    buy_time = timestamp_to_strtime(i["T"])
                    print "it's a big buy item,  buy price is %s, buy mount is %s" %(i["p"],i["q"])
                    print "the big buy item's time is %s" %buy_time
            else:
                all_sell_price = all_buy_price + float(i["p"]) * float(i["q"])
                all_sell_amount = all_buy_amount + float(i["q"])
                if float(i["q"]) > strd_amount:
                    sell_time = timestamp_to_strtime(i["T"])
                    print "it's a big sell item, sell price is %s, sell mount is %s" %(i["p"],i["q"])
                    print "the big sell item's time is %s" %sell_time
    print "total buy price is %f" %all_buy_price
    print "total buy amount is %f" %all_buy_amount
    print "total sell price is %f" %all_sell_price
    print "total sell amount is %f" %all_sell_amount

def timestamp_to_strtime(timestamp):
    local_str_time = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
    return local_str_time

get_big_trade()