"""
coinbase-advanced-py


Code fonctionnel

"""



from coinbase.rest import RESTClient
import json

# Initialiser le client REST avec votre clé d'API Coinbase
client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")

# Remplacer "DYP" par le symbole de la crypto-monnaie que vous souhaitez vendre
crypto_symbol = "DYP"


accounts = client.get_accounts()


matching_account = None

for account in accounts["accounts"]:
    if account['currency'] == crypto_symbol:
        matching_account = account
        break

if matching_account:
    print("Compte correspondant au symbole {} trouvé:".format(crypto_symbol))
    print(matching_account)
else:
    print("Aucun compte correspondant au symbole {} trouvé.".format(crypto_symbol))



sell_quantity = matching_account["available_balance"]["value"]


#order = client.market_order_sell(client_order_id = "ordre001", product_id = "DYP-USDC", base_size = "14")


