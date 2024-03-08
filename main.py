from fonctions_crypto import *
import cryptocompare
import time

from send_email_file import *

from specials_alerts import *
from class_crypos import *

from log import *

loop_intervall_seconds = 60*5

# set global variable MODE to real (the test mode can be use for test purpose)
set_variable_mode("real")                  # real  / test

# Set up CRYPTOS object
CRYPTOS_object = CRYPTOS()
CRYPTOS_object.getCRYPTO_json()

# reset maximums prices for peak detection
#CRYPTOS_object.cryptos_reset_max_price()

# set the number of notification authorized for a crypto
CRYPTOS_object.cryptos_set_notifications_authorisations(10)

# set USDC blance to 0
#CRYPTOS_object.initialise_all_USDC_balance()

# Refresh the amount of crypto from coinbase API
CRYPTOS_object.actualise_crypto_account()

# Set detection variables
CRYPTOS_object.set_crypto_peak_target(99)
CRYPTOS_object.set_crypto_break_even_point(103)



"""
Main loop
"""
while True :

    print("Start loop : ", time.strftime("%a %b %d %Y - %H:%M:%S"))
    write_log("info", "Start loop")

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
        minor_error(f"Cannot write in crypto userfriendly: {str(e)}")

    # specials alerts
    #specials_alerts(CRYPTOS)

    """
    End of the loop
    """
    print("End loop : ", time.strftime("%a %b %d %Y - %H:%M:%S"))
    write_log("info", "End loop")
    
    # sleep (seconds)
    time.sleep(loop_intervall_seconds)





