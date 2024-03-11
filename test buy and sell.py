


"""
This code works fins and honeys were bought
"""



from coinbase.rest import RESTClient

client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
value = client.get_product("AERO-USD")
acounts = client.get_accounts()

product_id = "DOGE-USDC"
amount = "5"

order = client.preview_market_order_buy(product_id = product_id, quote_size = amount)
order = client.market_order_buy(client_order_id = "ordre001", product_id = product_id, quote_size = amount)
#order = client.market_order_sell(client_order_id = "ordre001", product_id = product_id, base_size = amount)
print(order)
