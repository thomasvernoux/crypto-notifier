"""
Smples functions linked to crypto
Author : Thomas Vernoux
Date : March 3, 2024
"""


import time
from global_variables import *
import cryptocompare
from pycoingecko import CoinGeckoAPI
import traceback

import functions_log
from functions_log import *

import functions_CoinBaseApi
from functions_CoinBaseApi import *

import class_cryptos

import inspect




time_notif_interval = 5 * 60  # interval between 2 notofications : 10 min


def get_price(crypto):
    """
    Get price :
    try to use coinbase API
    """



    log_trace(str(inspect.currentframe().f_back.f_code.co_name))

    if Variable("coinbase_api_call_activated").get(): 
        try : 
            price = functions_CoinBaseApi.get_sell_price_coinabse_api(crypto)

            if isinstance(price, float):
                #print ("Crypto getprice : ", crypto.name)
                functions_log.log_write("crypto getprice", f"getprice : {crypto.name} , {crypto.current_price}\n")

                return price
        
            else : 
                error_message = f"price is not a float : {crypto.name}  \n{tb}"
                print(error_message)
                log_error_critic(error_message)


        except Exception as e:
            tb = traceback.format_exc()
            error_message = f"error in get_price(crypto) : {crypto.name}  \n{tb}"
            print(error_message)
            log_error_critic(error_message)
    
    else : 
        # Variable("coinbase_api_call_activated").get() set to False
        return 1000

def depreciated_get_price(crypto, NumberOfReccursion : int = 3):
    """
    Get price :
    try to use coinbase API , then coingecko to get the price, if it is not possible, try with cryptocompare
    Reccursiv function

    TODO : remake this function
    """



    log_trace(str(inspect.currentframe().f_back.f_code.co_name))

    if Variable("coinbase_api_call_activated").get(): 

        if NumberOfReccursion < 1 :
            error_message = "Critical error : get_price, functions_crypto : NumberOfReccursion < 1"
            print(error_message)
            log_error_critic(error_message)
        
        price = None
        
        try : 
            price = get_sell_price_coinabse_api(crypto)
        except :
            message = f"cannot get price from coinbase api, crypto : {crypto}\nTry again, reccursivity : {NumberOfReccursion}"
            log_error_minor(message)
            print(message)
            get_price(crypto, NumberOfReccursion -1)
            


        if isinstance(price, float):
            #print ("Crypto getprice : ", crypto.name)
            log_write("crypto getprice", f"getprice : {crypto.name} , {crypto.current_price}\n")

            return price
        else:
            message = f"cannot get price from coinbase api, crypto : {crypto.get_crypto_info_str()}\nTry again, reccursivity : {NumberOfReccursion}"
            log_error_minor(message)
            print(message)
            get_price(crypto, NumberOfReccursion -1)

        return None
    
    else : 
        return 1000

def refresh_crypto_data():
    """
    If change detected, refresh crypto data
    """

    # Set the flag back to False
    Variable("extern_change_detected").set(False)

    CRYPTOS_object = class_cryptos.CRYPTOS()
    CRYPTOS_object.getCRYPTO_json()

    # Refresh the amount of crypto from coinbase API
    CRYPTOS_object.actualise_crypto_account()

    # Refresh buy prices
    CRYPTOS_object.set_buy_prices()

    # update USDC Balance
    CRYPTOS_object.initialise_all_USDC_balance()

    # Set detection variables
    CRYPTOS_object.set_crypto_peak_target(99)
    CRYPTOS_object.set_crypto_break_even_point(Variable("break_even_point").get())

    # Save data
    CRYPTOS_object.writeCRYPTO_json()

def setup_crypto():
    """
    Setup crypto parameters
    """

    # Set up CRYPTOS object
    CRYPTOS_object = class_cryptos.CRYPTOS()
    CRYPTOS_object.getCRYPTO_json()

    # reset maximums prices for peak detection
    #CRYPTOS_object.cryptos_reset_max_price()

    # set the number of notification authorized for a crypto
    CRYPTOS_object.cryptos_set_notifications_authorisations(20)

    # Refresh buy prices
    CRYPTOS_object.set_buy_prices()

    # update USDC blance
    CRYPTOS_object.initialise_all_USDC_balance()

    # Set detection variables
    CRYPTOS_object.set_crypto_peak_target(99)
    CRYPTOS_object.set_crypto_break_even_point(Variable("break_even_point").get())

    # Save data
    CRYPTOS_object.writeCRYPTO_json()

    return 


