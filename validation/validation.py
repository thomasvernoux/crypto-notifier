

import sys
sys.path.append('./')

import os
import shutil

import process_peak_detection


from functions_crypto import *
import cryptocompare
import time
from functions_email import *
from global_variables import *
from class_cryptos import *
from functions_log import *

Variable("mode").set("test")
Variable("sound_activated").set(False)

all_test_passed = True




def test_sell_001():
    """
    Test the sell functionnality
    Date : 2024/05/09
    Author : Thomas
    """

    global all_test_passed

    CRYPTOS_object = CRYPTOS()
    
    crypto = Crypto()
    crypto.name = "Test"
    crypto.coinbaseId = "Test"
    crypto.name_cryptocompare = None
    crypto.name_coingecko = None
    crypto.amount = 1
    crypto.last_order_buy_price = 100
    crypto.last_order_buy_datetime = None
    crypto.max_price = 120
    crypto.current_price = 110
    crypto.USDC_balance = 1
    crypto.number_of_alert_authorized = None
    crypto.last_notification_time = None
    crypto.peak_target = 99
    crypto.break_even_point = 101
    crypto.profit_percent = None
    crypto.last_buy_order = None


    CRYPTOS_object.cryptos_list = [crypto]

    

    directory = "CRYPTO json/"
    try:
        shutil.rmtree(directory)
        #print(f"Le répertoire {directory} a été supprimé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression du répertoire : {e}")


    CRYPTOS_object.writeCRYPTO_json()




    process_peak_detection.ProcessPeakDetection()

    if Variable("test_variable_sell_order_done").get():
        None
    else : 
        all_test_passed = False

    directory = "CRYPTO json/"
    try:
        shutil.rmtree(directory)
        print(f"Le répertoire {directory} a été supprimé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression du répertoire : {e}")














test_sell_001()


print("All tests passed : ", all_test_passed)
