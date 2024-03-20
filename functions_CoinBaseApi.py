"""
Functions linked to the Coinbase API
Author : Thomas Vernoux
Date : March 3, 2024
"""


from coinbase.rest import RESTClient
from coinbase.rest.products import get_product

# Old api
from coinbase.wallet.client import Client

import json
from global_variables import *

from functions_basics import *
from functions_log import *

import inspect

"""
API rate limit : https://docs.cloud.coinbase.com/advanced-trade-api/docs/rest-api-rate-limits
"""

def load_var_from_json(filename, variable):
    """
    Load a variable from json
    @filename : path to json
    @variable : name of the variable to find in the json
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    global_lock = global_lock_get()
    with global_lock :
        with open(filename, 'r') as file:
            keys = json.load(file)
    return keys[variable]




def get_accounts_from_api_OLD():
    api_key  = load_var_from_json('api_keys/api_key_001.json', "api_key")
    api_secret = load_var_from_json('api_keys/api_key_001.json', "api_secret")
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    client = Client(api_key, api_secret)
    user = client.get_current_user()
    #print(user)
    p = client.get_buy_price(currency_pair = 'BTC-USD')
    #print(p)


    accounts = client.get_accounts()

    for i in accounts["data"] : 
        log_write("coinbase api call history", f"{i}\n")
        
    log_write("coinbase api call history", f"\n")

    return accounts

def get_accounts_from_api():
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
    accounts = client.get_accounts()["accounts"]
    

    for i in accounts : 
        log_write("coinbase api call history", f"{i}\n")
        
    log_write("coinbase api call history", f"\n")

    return accounts

def update_account_id_dico():
    api_key  = load_var_from_json('api_keys/api_key_001.json', "api_key")
    api_secret = load_var_from_json('api_keys/api_key_001.json', "api_secret")
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    client = Client(api_key, api_secret)
    accounts = client.get_accounts()
    
    global dico_account_id
    dico_account_id = {}
    for i in accounts["data"]:
        key = i.currency.code
        value = i.currency.asset_id
        dico_account_id[key] = value

    Variable("dico_account_id").set(dico_account_id)

def sell_crypto_for_USDC(crypto_symbol):
    """
    Request API for selling the maximum of the parameter crypto
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
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
        log_error_critic(message)



    product_id = f"{crypto_symbol}-USDC"
    available_sell_quantity = matching_account["available_balance"]["value"]
    if available_sell_quantity == '':
        log_error_minor("available_sell_quantity == ''")
        print("available_sell_quantity == '', error rised")
        Variable("extern_change_detected").set(True)
        return False
    
    try :  
        # Get the specifiities of the product (increment)
        product = client.get_product(product_id)
        available_sell_quantity = calculate_sell_quantity(product, available_sell_quantity)
    
    except Exception as e :
        tb = traceback.format_exc()
        log_error_minor(tb)
    
    #binary_confirmation(f"Your are selling {available_sell_quantity} of {product_id}. Process ?")
    preview_order = client.preview_market_order_sell(product_id = product_id, base_size = available_sell_quantity)
    if preview_order["errs"] != []:
        print("errors detected in preview order")
        log_write("sell order history",
                   f"Errors detected in preview order : \n{str(preview_order['errs'])}", 
                   persistant= True)
    
    if Variable("coinbase_api_sell_activated").get():
        log_write("sell order history",
                   f"""market order sell send. Parameters :
                   client_order_id : {str(preview_order["errs"])}
                   product_id : {product_id}
                   base size : {available_sell_quantity}\n""", 
                   persistant= True)
        order = client.market_order_sell(client_order_id = "OrderByPython" + str(time.time()), product_id = product_id, base_size = available_sell_quantity)
        print("order : ", order)
        print("preview order : " , preview_order)
        log_write("sell order history", "order_variable recieved from coinbase api :\n" + str(order), persistant=True)
        

        log_write("debug_order", f"parameters - product id : {product_id}, available_sell_quantity : {available_sell_quantity}")
        log_write("debug_order", "preview order : " + str(order))
        log_write("debug_order", "order : " + str(order))


    elif Variable("mode").get() == "test":
        None
        
        
    return order

def get_sell_price_coinabse_api(crypto, iteration_number = 0):
    
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    if crypto.coinbaseId == None :
        log_error_minor(f"crypto : {crypto.name} has no coinbaseId")
        print(f"La crypto-monnaie {crypto.name} n'a pas de coinbaseId.")
        raise ValueError(f"La crypto-monnaie {crypto.name} n'a pas de coinbaseId.")
        

    client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
    product_id = f"{crypto.coinbaseId}-USDC"
    crypto_price = float(client.get_product(product_id)["price"])

    if crypto_price == None : 
        if Variable("recursiv_call_number").get() > 5 :
            log_error_critic("cannot get crypto price with coinbase api. 5 recursiv call were done, and the price is still None")
        else : 
            Variable("recursiv_call_number").set((Variable("recursiv_call_number").get() + 1))
            crypto_price = get_sell_price_coinabse_api(crypto)

    return crypto_price

    






















