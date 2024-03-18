



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
        while get_variable_program_on():
            print("ProcessUpdatePrice_ALL loop")
            
            CRYPTOS_object = CRYPTOS()
            CRYPTOS_object.getCRYPTO_json()
            
            for i in range (len(CRYPTOS_object.cryptos_list)):
                if get_variable_run_mode().coinbase_api_getprice_activated:
                    CRYPTOS_object.cryptos_list[i].current_price = get_price(CRYPTOS_object.cryptos_list[i])

                """
                Update USDC Balance
                """
                CRYPTOS_object.cryptos_list[i].update_USDC_balance()

                """
                Update max price
                """
                CRYPTOS_object.cryptos_list[i].update_max_price()

            CRYPTOS_object.writeCRYPTO_json()

            time.sleep(get_variable_time_loop_update_price_all_process())


    except KeyboardInterrupt:
        print("Keyboard interruption detected. End of ProcessUpdatePrice_ALL")

def ProcessUpdatePrice():
    """
    Update crypto price is > 0.5 USDC
    """

    try:
        while get_variable_program_on():
            print("ProcessUpdatePrice loop")
            
            CRYPTOS_object = CRYPTOS()
            CRYPTOS_object.getCRYPTO_json()
            
            for i in range (len(CRYPTOS_object.cryptos_list)):
                if CRYPTOS_object.cryptos_list[i].USDC_balance > 0.5:
                    if get_variable_run_mode().coinbase_api_getprice_activated :
                        CRYPTOS_object.cryptos_list[i].current_price = get_price(CRYPTOS_object.cryptos_list[i])

                    """
                    Update USDC Balance
                    """
                    CRYPTOS_object.cryptos_list[i].update_USDC_balance()

                    """
                    Update max price
                    """
                    CRYPTOS_object.cryptos_list[i].update_max_price()

            CRYPTOS_object.writeCRYPTO_json()

            time.sleep(get_variable_time_loop_update_price_process())


    except KeyboardInterrupt:
        set_variable_program_on(False)
        print("End of ProcessUpdatePrice")



