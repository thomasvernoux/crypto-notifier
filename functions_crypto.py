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
from functions_log import *
from functions_CoinBaseApi import *

import class_cryptos





time_notif_interval = 5 * 60  # interval between 2 notofications : 10 min





def time_interval(crypto):
    """
    Check time intervall between two notification requests
    retrn true or false if the notification can be done
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    if (time.time() > crypto.last_notification_time + time_notif_interval) or (crypto.last_notification_time == 0):
        return True
    return False

def get_crypto_price_cryptocompare(crypto):
    """
    Get price from cryptocompare API
    """

    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    if crypto.name_cryptocompare == None : 
        #print ("no name cryptocompare for : ", crypto.name)
        log_write("get_price_status", f"no name cryptocompare for : {crypto.name}\n")
        log_error_minor("cannot get price for crypto : \n" + crypto.get_crypto_info_str())
        print("name cryptocompare not defined")
        return None

    # Ouvrez le fichier contenant le compteur
    with open("api_counter/counter_cryptocompare.txt", "r+") as file:
        count = int(file.read() or 0)  # Lisez le compteur actuel ou initialisez-le à zéro
        count += 1  # Incrémentez le compteur
        file.seek(0)  # Déplacez le curseur au début du fichier
        file.write(str(count))  # Écrivez le nouveau compteur dans le fichier
        file.truncate()  # Tronquez le fichier au cas où le nouveau compteur est plus court que l'ancien


    return cryptocompare.get_price(crypto.name_cryptocompare, 'USD')[crypto.name_cryptocompare]["USD"]

def get_crypto_price_coingecko(crypto):
    """
    Get price from coingecko api

    Is CoinGecko API free?
    CoinGecko API offers both free and paid plans. 
    The Demo API plan is accessible to all CoinGecko users at zero cost, 
    with a stable rate limit of 30 calls/min and a monthly cap of 10,000 calls.

    = 13 calls per hours
    """

    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    if crypto.name_coingecko == None : 
        #print ("no name coingecko for : ", crypto.name)
        log_write("get_price_status", f"no name coingecko for : {crypto.name}\n")
        log_error_minor("cannot get price for crypto : \n" + crypto.get_crypto_info_str())
        print("name coingecko not defined")
        return None

    # compteur d'utilisation de l'api pygecko
    # Ouvrez le fichier contenant le compteur
    with open("api_counter/counter_coingecko.txt", "r+") as file:
        count = int(file.read() or 0)  # Lisez le compteur actuel ou initialisez-le à zéro
        count += 1  # Incrémentez le compteur
        file.seek(0)  # Déplacez le curseur au début du fichier
        file.write(str(count))  # Écrivez le nouveau compteur dans le fichier
        file.truncate()  # Tronquez le fichier au cas où le nouveau compteur est plus court que l'ancien



    cg = CoinGeckoAPI()
    return cg.get_price(ids=crypto.name_coingecko, vs_currencies='usd')[crypto.name_coingecko]["usd"]

def get_price(crypto, NumberOfReccursion : int = 3):
    """
    Get price :
    try to use coinbase API , then coingecko to get the price, if it is not possible, try with cryptocompare
    Reccursiv function
    """

    log_trace(str(inspect.currentframe().f_back.f_code.co_name))

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
    CRYPTOS_object.set_crypto_break_even_point(103)

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
    CRYPTOS_object.set_crypto_break_even_point(103)

    # Save data
    CRYPTOS_object.writeCRYPTO_json()

    return 


