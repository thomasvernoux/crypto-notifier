
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

        """
        TODO 
        revoir cette fonction set buy price qui est torp vieille et fais redondance avec update last order for each crypto
        """
        """
        Doto : manage le buy price
        """
        #CRYPTOS_object.set_buy_prices()

        CRYPTOS_object.update_last_order_for_each_crypto()

        CRYPTOS_object.writeCRYPTO_json()



    except KeyboardInterrupt:
        print("End of ProcessUpdateAccount")

    




    