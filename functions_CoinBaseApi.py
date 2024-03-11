
from coinbase.rest import RESTClient
from coinbase.rest.products import get_product

# Old api
from coinbase.wallet.client import Client

import json
from global_variables import *

from functions_basics import *
from functions_log import *

"""
API rate limit : https://docs.cloud.coinbase.com/advanced-trade-api/docs/rest-api-rate-limits
"""

def load_var_from_json(filename, variable):
    """
    Load a variable from json
    @filename : path to json
    @variable : name of the variable to find in the json
    """
    with open(filename, 'r') as file:
        keys = json.load(file)
    return keys[variable]

api_key  = load_var_from_json('api_keys/api_key_001.json', "api_key")
api_secret = load_var_from_json('api_keys/api_key_001.json', "api_secret")

def get_accounts_from_api_OLD():

    client = Client(api_key, api_secret)
    user = client.get_current_user()
    #print(user)
    p = client.get_buy_price(currency_pair = 'BTC-USD')
    #print(p)


    accounts = client.get_accounts()

    for i in accounts["data"] : 
        write_log("coinbase api call history", f"{i}\n\n\n\n")
        
    write_log("coinbase api call history", f"\n")

    return accounts

def get_accounts_from_api():

    client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
    accounts = client.get_accounts()["accounts"]
    

    for i in accounts : 
        write_log("coinbase api call history", f"{i}\n\n\n\n")
        
    write_log("coinbase api call history", f"\n")

    return accounts

def update_account_id_dico():
    client = Client(api_key, api_secret)
    accounts = client.get_accounts()
    
    global dico_account_id
    dico_account_id = {}
    for i in accounts["data"]:
        key = i.currency.code
        value = i.currency.asset_id
        dico_account_id[key] = value

    set_variable_dico_account_id(dico_account_id)

def sell_crypto_for_USDC(crypto_symbol):
    """
    Request API for selling the maximum of the parameter crypto
    """

    # Initialiser le client REST avec votre clé d'API Coinbase
    client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")

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
        message = "Aucun compte correspondant au symbole {} trouvé.".format(crypto_symbol)
        print(message)
        critical_error(message)



    product_id = f"{crypto_symbol}-USDC"
    available_sell_quantity = matching_account["available_balance"]["value"][:-1]
    available_sell_quantity = truncate_number(available_sell_quantity, significant_digits=3)
    
    
    #binary_confirmation(f"Your are selling {available_sell_quantity} of {product_id}. Process ?")
    if get_variable_mode() == "real":
        order = client.market_order_sell(client_order_id = "ordre001", product_id = product_id, base_size = available_sell_quantity)
        print(order)
        write_log("sell order history", str(order))

    elif get_variable_mode() == "test":
        order = client.preview_market_order_sell(product_id = product_id, base_size = available_sell_quantity)
        print(order)
        
        
    return order

def get_sell_price_coinabse_api(crypto):
    if crypto.coinbaseId == None :
        minor_error(f"crypto : {crypto.name} has no coinbaseId")
        print(f"La crypto-monnaie {crypto.name} n'a pas de coinbaseId.")
        raise ValueError(f"La crypto-monnaie {crypto.name} n'a pas de coinbaseId.")
        

    client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
    product_id = f"{crypto.coinbaseId}-USDC"
    crypto_price = float(client.get_product(product_id)["price"])


    return crypto_price

    






















