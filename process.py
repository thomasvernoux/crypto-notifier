from functions_crypto import *
import time

from functions_email import *

from functions_specials_alerts import *
from class_cryptos import *

from functions_log import *


from process import *


def process():
    """
    Process the crypto-notifier programm
    """

    loop_intervall_seconds = 60 * 5

    # set global variable MODE to real (the test mode can be use for test purpose)
    set_variable_mode("real")                  # real  / test
    set_variable_sound_activated(True)

    # Set up CRYPTOS object
    CRYPTOS_object = CRYPTOS()
    CRYPTOS_object.getCRYPTO_json()

    # reset maximums prices for peak detection
    #CRYPTOS_object.cryptos_reset_max_price()

    # set the number of notification authorized for a crypto
    CRYPTOS_object.cryptos_set_notifications_authorisations(2)

    # Refresh the amount of crypto from coinbase API
    CRYPTOS_object.actualise_crypto_account()

    # Refresh buy prices
    CRYPTOS_object.set_buy_prices()

    # set USDC blance to 0
    CRYPTOS_object.initialise_all_USDC_balance()

    # Set detection variables
    CRYPTOS_object.set_crypto_peak_target(99)
    CRYPTOS_object.set_crypto_break_even_point(103)

    # Save data
    CRYPTOS_object.writeCRYPTO_json()



    """
    Main loop
    """
    while True :
        
        # Get Crypto object
        CRYPTOS_object = CRYPTOS()
        CRYPTOS_object.getCRYPTO_json()
        
        print("Start loop : ", time.strftime("%a %b %d %Y - %H:%M:%S"))
        log_write("info", "Start loop")

        for crypto in CRYPTOS_object.cryptos_list:


            if (crypto.amount == 0) :
                continue 
            # Process each crypto
            if (crypto.USDC_balance >= 1) : 
                crypto.cryptoprocess()
            
        # Save data into files
        CRYPTOS_object.writeCRYPTO_json()

        try : 
            CRYPTOS_object.writeCRYPTO_userfriendly()
        except Exception as e:
            log_error_minor(f"Cannot write in crypto userfriendly: {str(e)}")

        # specials alerts
        #specials_alerts(CRYPTOS)

        """
        End of the loop
        """
        print("End loop : ", time.strftime("%a %b %d %Y - %H:%M:%S"))
        log_write("info", "End loop")
        
        # sleep (seconds)
        time.sleep(loop_intervall_seconds)





