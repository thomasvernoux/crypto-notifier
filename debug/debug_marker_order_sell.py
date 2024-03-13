"""
Debug market order sell
debug en cours
"""

"""
Base size : C'est la quantité de la crypto-monnaie de base dans une paire de trading. 
Par exemple, dans la paire BTC/USD, la base size serait la quantité de Bitcoin (BTC) échangée.

Quote size : C'est la quantité de la crypto-monnaie cotée dans une paire de trading. 
Dans la paire BTC/USD, la quote size serait la quantité de dollars américains (USD) échangée.
"""




import sys
sys.path.append('./')

from class_cryptos import *
from functions_basics import *





set_variable_mode("real")
crypto = Crypto()
crypto.name = "PNG"

"""
Buy some crypto
"""

product_id = f"{crypto.name}-USDC"
crypto_qty = "3"


client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
preview_order = client.preview_market_order_buy(product_id = product_id, base_size = crypto_qty)
quote_size = preview_order["quote_size"]
print(preview_order)
#order_b = client.market_order_buy(client_order_id = "test02", product_id = product_id, quote_size = quote_size)
#print(order_b)


accounts = client.get_accounts()


matching_account = None
for account in accounts["accounts"]:
    if account['currency'] == crypto.name:
        matching_account = account
        break


product = client.get_product(product_id)
print(product)

v = matching_account["available_balance"]["value"]
sell_sty = calculate_sell_quantity(product, v)
sell_qty_str = str(sell_sty)




preview_order_s = client.preview_market_order_sell(product_id = product_id, base_size = sell_qty_str)
print(preview_order_s)
order_s = client.market_order_sell(client_order_id = "ordre001", product_id = product_id, base_size = sell_qty_str)
print(order_s)

#order = crypto.sell_for_USDC()






#test_sell_for_USDC()

