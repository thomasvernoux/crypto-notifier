
"""
Process function updating account
Author : Thomas Vernoux
Date : 2024/03/15

Update account
Update last buy price
"""

import time

from functions_crypto import *
from functions_email import *
from functions_specials_alerts import *
from functions_log import *
from class_cryptos import *

import inspect


def ProcessUpdateAccount():

    

    try:
        log_write("working process", "ProcessUpdateAccount")
        
        CRYPTOS_object = CRYPTOS()
        CRYPTOS_object.getCRYPTO_json()
        CRYPTOS_object.actualise_crypto_account()

        CRYPTOS_object.set_buy_prices()

        CRYPTOS_object.writeCRYPTO_json()



    except KeyboardInterrupt:
        print("End of ProcessUpdateAccount")

    




    