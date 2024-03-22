



import time

from functions_crypto import *
from functions_email import *
from functions_specials_alerts import *
from functions_log import *
from class_cryptos import *
from functions_basics import *

import inspect



def ProcessUpdatePrice_ALL():
    """
    Update all prices
    """

    

    try:
        if Variable("program_on").get():
            print("ProcessUpdatePrice_ALL loop")
            log_write("working process", "ProcessUpdatePrice_ALL")
            
            CRYPTOS_object = CRYPTOS()
            CRYPTOS_object.getCRYPTO_json()
            
            for i in range (len(CRYPTOS_object.cryptos_list)):
                if Variable("coinbase_api_getprice_activated").get() :
                    CRYPTOS_object.cryptos_list[i].current_price = get_price(CRYPTOS_object.cryptos_list[i])

                """
                Update USDC Balance
                """
                CRYPTOS_object.cryptos_list[i].update_USDC_balance()

                """
                Update max price
                """
                CRYPTOS_object.cryptos_list[i].update_max_price()

                """
                Store to SQLite database
                """
                functions_SQLite.add_value(crypto_name = CRYPTOS_object.cryptos_list[i].name, data_tuple = (time.time(),CRYPTOS_object.cryptos_list[i].current_price))

            CRYPTOS_object.writeCRYPTO_json()

            time.sleep(Variable("time_loop_update_price_all_process").get())


    except KeyboardInterrupt:
        print("Keyboard interruption detected. End of ProcessUpdatePrice_ALL")

def ProcessUpdatePrice():
    """
    Update crypto price is > 0.5 USDC
    Update max price
    Write price to SQL database
    """

    log_write("working process", "ProcessUpdatePrice")

    try:
        if Variable("program_on").get():
            print("ProcessUpdatePrice loop")
            
            CRYPTOS_object = CRYPTOS()
            CRYPTOS_object.getCRYPTO_json()
            
            for i in range (len(CRYPTOS_object.cryptos_list)):
                if CRYPTOS_object.cryptos_list[i].USDC_balance > 0.5:
                    if Variable("coinbase_api_getprice_activated").get() :
                        CRYPTOS_object.cryptos_list[i].current_price = get_price(CRYPTOS_object.cryptos_list[i])

                    """
                    Update USDC Balance
                    """
                    CRYPTOS_object.cryptos_list[i].update_USDC_balance()

                    """
                    Update max price
                    """
                    CRYPTOS_object.cryptos_list[i].update_max_price()

                    """
                    Store to SQLite database
                    """
                    functions_SQLite.add_value(crypto_name = CRYPTOS_object.cryptos_list[i].name, data_tuple = (time.time(),CRYPTOS_object.cryptos_list[i].current_price))

            CRYPTOS_object.writeCRYPTO_json()

            time.sleep(Variable("time_loop_update_price_process").get())


    except KeyboardInterrupt:
        Variable("program_on").set(False)
        print("End of ProcessUpdatePrice")



