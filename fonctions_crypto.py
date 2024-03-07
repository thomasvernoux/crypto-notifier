
import time
from global_variables import *
import cryptocompare
from pycoingecko import CoinGeckoAPI
import traceback
from log import *



time_notif_interval = 5 * 60  # interval between 2 notofications : 10 min





def time_interval(crypto):
    """
    Check time intervall between two notification requests
    retrn true or false if the notification can be done
    """
    if (time.time() > crypto.last_notification_time + time_notif_interval) or (crypto.last_notification_time == 0):
        return True
    return False

def get_crypto_price_cryptocompare(crypto):
    """
    Get price from cryptocompare API
    """

    if crypto.name_cryptocompare == None : 
        #print ("no name cryptocompare for : ", crypto.name)
        write_log("get_price_status", f"no name cryptocompare for : {crypto.name}\n")
        minor_error("cannot get price for crypto : \n" + crypto.get_crypto_info_str())
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

    if crypto.name_coingecko == None : 
        #print ("no name coingecko for : ", crypto.name)
        write_log("get_price_status", f"no name coingecko for : {crypto.name}\n")
        minor_error("cannot get price for crypto : \n" + crypto.get_crypto_info_str())
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

def get_price(crypto):
    """
    Get price :
    try to use coingecko to get the price, if it is not possible, try with cryptocompare
    """


    price = None
    try :
        price = get_crypto_price_coingecko(crypto)
    except Exception : 
        print ("coingecko error")
        traceback.print_exc()


        try : 
                price = get_crypto_price_cryptocompare(crypto)
        except Exception: 
            print ("cryptocompare error")
            traceback.print_exc()



    if isinstance(price, float):
        #print ("Crypto getprice : ", crypto.name)
        write_log("crypto getprice", f"getprice : {crypto.name} , {crypto.current_price}\n")
        return price
    else:
        critical_error("crypto price is not float : \n" + crypto.get_crypto_info_str())



    


