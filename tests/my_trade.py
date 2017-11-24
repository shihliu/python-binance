from binance.client import Client
import json
client = Client('yq67cDjrCxGl6eeKMyTeiK1zkeArFpu8v4uB4b6TWDQdgjDlH0KjmXfHBZ1NjvJj', 'DxE7Wugo75EK8mLmybY76dbZW6tROpyNjBRd9NHsEOXqBaKq6Awgul4390xwRUdc')

my_trade = client.get_my_trades(symbol='QSPETH')

all_buy_price = all_buy_amount= 0.0
all_sell_price = all_sell_amount= 0.0

for i in my_trade:
    if i["isBuyer"] is True:
        all_buy_price = all_buy_price + float(i["price"]) * float(i["qty"])
        all_buy_amount = all_buy_amount + float(i["qty"])
    else:
        all_sell_price = all_buy_price + float(i["price"]) * float(i["qty"])
        all_sell_amount = all_buy_amount + float(i["qty"])
avg_buy_price = all_buy_price / all_buy_amount
print "my total buy price is %f" %all_buy_price
print "my total buy amount is %f" %all_buy_amount
print "average buy price is %f" %avg_buy_price
avg_sell_price = all_sell_price / all_sell_amount
print "my total sell price is %f" %all_sell_price
print "my total sell amount is %f" %all_sell_amount
print "average sell price is %f" %avg_sell_price