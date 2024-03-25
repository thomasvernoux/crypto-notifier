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




def depreciated_process():
    """
    Process the crypto-notifier program
    """

    """
    ###
    SETUP
    ###
    """
    """
    VARIABLES
    """

    loop_intervall_seconds = 60                 # Second intervall between two loops

    # MODE to real (the test mode can be use for test purpose)
    Variable("mode").set("real")                   # real  / test
    Variable("sound_activated").set(False)         # Global variable for sound. Used when a crypto is sell
    Variable("extern_change_detected").set(False)
    Variable("recursiv_call_number").set(0)
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
        
        if Variable("extern_cnahge_detected").get():
            
            # Set the flag back to False
            Variable("extern_cnahge_detected").set(False)

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





