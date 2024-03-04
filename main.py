from fonctions_crypto import *
import cryptocompare
import time

from send_email_file import *
from cryptoprocess import *
from specials_alerts import *


# reset maximums prices for peak detection
cryptos_reset_max_price()

# set the number of notification authorized for a crypto
cryptos_set_notifications_authorisations(10)

# Get crypto values
CRYPTOS = getCRYPTO()

# set global variable MODE to real (the test mode can be use for test purpose)
set_variable_mode("real")                  # real  / test

"""
Main loop
"""
while True :

    print("loop : ", time.strftime("%a %b %d %Y - %H:%M:%S"))

    for crypto in CRYPTOS:
        # Process each crypto
        crypto = crypto_process(crypto)
        
    # Save data into files
    writeCRYPTO(CRYPTOS)
    writeCRYPTO_userfriendly(CRYPTOS)

    # specials alerts
    #specials_alerts(CRYPTOS)


    print("end of the loop : ", time.strftime("%a %b %d %Y - %H:%M:%S"))
    
    # sleep (seconds)
    time.sleep(60 * 15)





