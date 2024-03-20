
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

from global_variables_lock_manager import *

import inspect


def ProcessUpdateAccount(global_lock):

    global_lock_set(global_lock)

    

    try:
        
        
        while Variable("program_on").get():

            log_write("working process", "ProcessUpdateAccount")

            """
            DEBUG
            """
            Continue = Variable("program_on")

            print("ProcessUpdateAccount")
            
            CRYPTOS_object = CRYPTOS()
            CRYPTOS_object.getCRYPTO_json()
            CRYPTOS_object.actualise_crypto_account()

            CRYPTOS_object.set_buy_prices()

            CRYPTOS_object.writeCRYPTO_json()

            time.sleep(Variable("time_loop_update_account_process").get())


    except KeyboardInterrupt:
        Variable("program_on").set(False)
        print("End of ProcessUpdateAccount")

    




    