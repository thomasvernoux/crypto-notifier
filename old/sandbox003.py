"""
Debug SHIB current price coingecko not correct
"""

from functions_crypto import *
from class_crypos import *
from functions_CoinBaseApi import *

from coinbase.rest.products import get_product



c = Crypto()
c.name_coingecko = "shiba-inu"
c.name_cryptocompare = "SHIB"
c.coinbaseId = "SHIB"

pcoin = get_crypto_price_coingecko(c)
pcryp = get_crypto_price_cryptocompare(c)

print(pcoin)
print(pcryp)

#pcoinbase = getprice_coinabse_api(c)

product_id = 'ETH-USDC'  # Remplacez 'BTC-USD' par l'identifiant du produit de votre crypto-monnaie
client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
crypto_price = client.get_product(product_id)

print(crypto_price)