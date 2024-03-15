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
from functions_basics import *

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

    setup_global_variables()


    """
    CRYPTOS OBJECT
    """

    setup_crypto()
    



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
            refresh_crypto_data()
            
        for crypto in CRYPTOS_object.cryptos_list:


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





