"""
Process function for crypto-notifier
Author : Thomas Vernoux
Date : 2024/03
"""

import time

from functions_crypto import *
from functions_email import *
from functions_specials_alerts import *
from functions_log import *
from class_cryptos import *

import inspect




def process():
    """
    Process the crypto-notifier program
    """

    log_trace(str(inspect.currentframe().f_back.f_code.co_name))

    

    """
    ###
    SETUP
    ###
    """
    """
    VARIABLES
    """

    loop_intervall_seconds = 30                 # Second intervall between two loops

    # MODE to real (the test mode can be use for test purpose)
    set_variable_mode("real")                   # real  / test
    set_variable_sound_activated(False)         # Global variable for sound. Used when a crypto is sell
    set_variable_extern_change_detected(False)
    set_variable_recursiv_call_number(0)
    set_variable_trace_activated(True)


    
    """
    CRYPTOS OBJECT
    """
    # Set up CRYPTOS object
    CRYPTOS_object = CRYPTOS()
    CRYPTOS_object.getCRYPTO_json()

    # reset maximums prices for peak detection
    #CRYPTOS_object.cryptos_reset_max_price()

    # set the number of notification authorized for a crypto
    CRYPTOS_object.cryptos_set_notifications_authorisations(20)

    # Refresh the amount of crypto from coinbase API
    CRYPTOS_object.actualise_crypto_account()

    # Refresh buy prices
    CRYPTOS_object.set_buy_prices()

    # update USDC blance
    CRYPTOS_object.initialise_all_USDC_balance()

    # Set detection variables
    CRYPTOS_object.set_crypto_peak_target(99)
    CRYPTOS_object.set_crypto_break_even_point(103)

    # Save data
    CRYPTOS_object.writeCRYPTO_json()



    """
    ###
    Main loop
    ###
    """
    while True :

        print("Start loop : ", time.strftime("%a %b %d %Y - %H:%M:%S"))
        log_write("info", "Start loop")
        
        # Get Crypto object
        CRYPTOS_object = CRYPTOS()
        CRYPTOS_object.getCRYPTO_json()

        """
        Detect extern changes
        """
        
        if get_variable_extern_change_detected():
            
            # Set the flag back to False
            set_variable_extern_change_detected(False)

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


        
        for crypto in CRYPTOS_object.cryptos_list:

            """
            DEBUG
            """
            if crypto.name == "ARB":
                a = 3


            if (crypto.amount == 0) :
                continue 
            # Process each crypto
            if (crypto.USDC_balance < 0.5) :
                continue 

            crypto.cryptoprocess()
            
        # Save data into files
        CRYPTOS_object.writeCRYPTO_json()

        
        CRYPTOS_object.writeCRYPTO_userfriendly()
        

        # specials alerts
        #specials_alerts(CRYPTOS)

        """
        End of the loop
        """
        print("End loop : ", time.strftime("%a %b %d %Y - %H:%M:%S"))
        log_write("info", "End loop")
        
        # sleep (seconds)
        time.sleep(loop_intervall_seconds)





