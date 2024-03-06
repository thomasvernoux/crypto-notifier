from fonctions_crypto import *
import cryptocompare
import time

from send_email_file import *

from specials_alerts import *
from class_crypos import *

from log import *


# set global variable MODE to real (the test mode can be use for test purpose)
set_variable_mode("real")                  # real  / test

# Set up CRYPTOS object
CRYPTOS_object = CRYPTOS()
CRYPTOS_object.getCRYPTO_json()

# reset maximums prices for peak detection
CRYPTOS_object.cryptos_reset_max_price()

# set the number of notification authorized for a crypto
CRYPTOS_object.cryptos_set_notifications_authorisations(10)

# Refresh the amount of crypto from coinbase API
CRYPTOS_object.actualise_crypto_account()

"""
Main loop
"""
while True :

    print("Start loop : ", time.strftime("%a %b %d %Y - %H:%M:%S"))
    write_log("info", "Start loop")

    for crypto in CRYPTOS_object.cryptos_list:
        # Process each crypto
        crypto.cryptoprocess()
        
    # Save data into files
    CRYPTOS_object.writeCRYPTO_json()

    try : 
        CRYPTOS_object.writeCRYPTO_userfriendly()
    except Exception as e:
        minor_error(f"Cannot write in crypto userfriendly: {str(e)}")

    # specials alerts
    #specials_alerts(CRYPTOS)


    print("End loop : ", time.strftime("%a %b %d %Y - %H:%M:%S"))
    write_log("info", "End loop")
    
    # sleep (seconds)
    time.sleep(60 * 15)





