
"""
Process function updating account
Author : Thomas Vernoux
Date : 2024/03/15
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
        
        while True:

            print("ProcessUpdateAccount")
            
            CRYPTOS_object = CRYPTOS()
            CRYPTOS_object.getCRYPTO_json()
            CRYPTOS_object.actualise_crypto_account()
            CRYPTOS_object.writeCRYPTO_json()

            time.sleep(get_variable_time_loop_update_account_process())


    except KeyboardInterrupt:
        print("Keyboard interruption detected. End of ProcessUpdateAccount")

    




    