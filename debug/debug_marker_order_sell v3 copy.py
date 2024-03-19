"""
Debug market order sell
"""

"""
Base size : C'est la quantité de la crypto-monnaie de base dans une paire de trading. 
Par exemple, dans la paire BTC/USD, la base size serait la quantité de Bitcoin (BTC) échangée.

Quote size : C'est la quantité de la crypto-monnaie cotée dans une paire de trading. 
Dans la paire BTC/USD, la quote size serait la quantité de dollars américains (USD) échangée.
"""



import time

import sys
sys.path.append('./')

from class_cryptos import *
from functions_basics import *





Variable("mode").set("real")
crypto = Crypto()
crypto.name = "VARA"

"""
Buy some crypto
"""

product_id = f"{crypto.name}-USDC"
USDC_qty = "1.1"


"""
BUY
"""

client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")

# preview_order = client.preview_market_order(product_id = product_id, quote_size = USDC_sty, side = "BUY")
# quote_size = preview_order["quote_size"]
# print(preview_order)
# client_order_id = str(time.time()).replace(".", "")
# order_b = client.market_order(client_order_id = f"client_order_id", product_id = product_id, quote_size = USDC_sty, side = "BUY")
# print(order_b)



"""
SELL
"""

product = client.get_product(product_id)
print(product)
precision = product["base_increment"]


#crypto.sell_for_USDC()
available_sell_quantity = "1e0"
#available_sell_quantity = decimal_to_precision(10.45, precision = precision)
order_preview = client.preview_market_order_sell(product_id = product_id, base_size = available_sell_quantity)
print("order_preview : ", order_preview)
order = client.market_order_sell(client_order_id = str(time.time()) + "ordre001", product_id = product_id, base_size = available_sell_quantity)
print("order : ", order)
a = 3



