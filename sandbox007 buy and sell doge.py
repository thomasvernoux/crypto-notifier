
"""
Le code a focntionné, les vara ont été vendues !
"""



from coinbase.rest import RESTClient

client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
value = client.get_product("AERO-USD")
acounts = client.get_accounts()

product = "VARA"
product_id = f"{product}-USDC"
crypto_amount = "11"

order1 = client.preview_market_order_sell(product_id = product_id, base_size = crypto_amount)
print(order1)
order = client.market_order_sell(client_order_id = "ordre001", product_id = product_id, base_size = crypto_amount)

print(order)




