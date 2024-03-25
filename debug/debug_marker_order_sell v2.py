"""
Debug market order sell
work fine
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





Variable("mode").set("real")
crypto = Crypto()
crypto.name = "SEAM"



product_id = f"{crypto.name}-USDC"
USDC_sty = "2.000"




client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")

product = client.get_product(product_id)
print(product)


crypto.sell_for_USDC()



