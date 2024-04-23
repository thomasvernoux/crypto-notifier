

from coinbase.rest import RESTClient
client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")

dict = client.list_orders(product_id="AVAX-USDC")['orders']
dict_orders = client.list_orders("AVAX-USDC")['orders']

a = 3


"""
Solution  : il n'y a pas d'ordres qui correspondent car c'est pas en USDC.
J'ai des AVAX mais via mon portefeuille en eur

"""