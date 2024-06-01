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

def get_accounts_from_api():

    if Variable("coinbase_api_call_activated").get():

        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
        accounts = client.get_accounts(250)["accounts"]


        for i in accounts : 
            log_write("coinbase api call history", f"{i}\n")
            
        log_write("coinbase api call history", f"\n")

        return accounts
    
    else : 
        return None

def sell_crypto_for_USDC(crypto_symbol):
    """
    Request API for selling the maximum of the parameter crypto
    """

    if Variable("sell_activated").get() :

        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        # Initialiser le client REST avec votre clé d'API Coinbase
        client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")

        accounts = client.get_accounts(250)


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
            return None
        
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

        
        log_write("sell order history",
                    f"""market order sell send. Parameters :
                    client_order_id : {str(preview_order["errs"])}
                    product_id : {product_id}
                    base size : {available_sell_quantity}\n""", 
                    persistant= True)
        order = client.market_order_sell(client_order_id = "Python Order" + str(time.time()), product_id = product_id, base_size = available_sell_quantity)
        print("order : ", order)
        print("preview order : " , preview_order)
        log_write("sell order history", "order_variable recieved from coinbase api :\n" + str(order), persistant=True)
        

        log_write("debug_order", f"parameters - product id : {product_id}, available_sell_quantity : {available_sell_quantity}")
        log_write("debug_order", "preview order : " + str(order))
        log_write("debug_order", "order : " + str(order))
  
        return order
    
    else : 
        log_write("sell order history", "Variable('sell_activated').get() == False, simulation mode. Sell order done")
        Variable("TEST_sell_order_done001").set(True)
        return None

def get_sell_price_coinabse_api(crypto, iteration_number = 0):
    
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))

    if Variable("coinbase_api_call_activated").get():
        
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
    
    else : 
        return 1000


def get_last_order(crypto):
    """
    Return the corresponding order (dict) for the crypto
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name) + f" {crypto.name}")



    if Variable("coinbase_api_call_activated").get():
        client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")

        try : 
            dict_orders = client.list_orders(f"{crypto.coinbaseId}-USDC")['orders']
        
        except : 
            try :
                # try a second time
                dict_orders = client.list_orders(f"{crypto.coinbaseId}-USDC")['orders']
        
            except Exception as e:
                tb = traceback.format_exc()
                error_message = f"error in get_last_order, functions_CoinbaseApi ({str(inspect.currentframe().f_back.f_code.co_name)})" + f" {crypto.name} \ntraceback : {tb}"
                print(error_message)
                log_error_critic(error_message)

        orders = []
        for order in dict_orders :
            orders.append(order)


        fitting_orders = []
        for i in orders : 
            ### Select right orders
            if not(i['product_id'] == f"{crypto.coinbaseId}-USDC"):
                continue
            if i['completion_percentage'] == 0:
                continue
            if i['side'] == "SELL" :
                continue
            if i['status'] != "FILLED" :
                continue
            
            fitting_orders.append(i)
        
        if fitting_orders == []:
            message = f"{str(inspect.currentframe().f_back.f_code.co_name)}, {crypto.name} No fitting order found for crypto : {crypto.name}"
            # The fitting_ordres variable can be [] if you have a crypto throught your eur != USDC wallet.
            #print(message)
            #log_error_minor(message)
            return None
        
        elif len(fitting_orders) == 1:
            return fitting_orders[0]

        elif len(fitting_orders) > 1:
            # find the last order
            the_last_oder = fitting_orders[0]
            for i in fitting_orders[1:]:
                if i['created_time'] > the_last_oder['created_time']:
                    the_last_oder = i
            price = float(the_last_oder['average_filled_price'])
            return the_last_oder
        

    else : 
        return None






















