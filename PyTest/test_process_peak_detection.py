"""
Date : 2024/05/14
Author : Thomas Vernoux

"""




import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Add the absolute path of the parent directory to sys.path
sys.path.append(parent_dir)




from global_variables import *

from functions_crypto import *
from process_peak_detection import *
from functions_basics import *

import shutil


Variable("sell_activated").set(False)  # test or real
Variable("coinbase_api_call_activated").set(False)  # test or real

def test_ProcessPeakDetection_001():
    """
    A simple test ProcessPeakDetection
    Peak should be detected
    """

    Variable("mail_activated").set(False)
    Variable("sell_activated").set(False)  # test or real
    Variable("coinbase_api_call_activated").set(False)  # test or real

    delete_directory_if_exists("CRYPTO json")

    crypto = Crypto()
    crypto.name = "BTC"
    crypto.coinbaseId = "BTC"
    crypto.current_price = 10
    crypto.amount = 10
    crypto.max_price = 12
    crypto.break_even_point = 101
    crypto.peak_target = 103
    crypto.USDC_balance = 20
    crypto.last_order_buy_price = 9

    crypto.write_variables_to_json_file()

    Variable("TEST_sell_order_done001").set(False)
    ProcessPeakDetection()

    assert Variable("TEST_sell_order_done001").get() == True

    Variable("TEST_sell_order_done001").set(False)

    delete_directory_if_exists("CRYPTO json")

def test_ProcessPeakDetection_002():
    """
    A simple test ProcessPeakDetection
    Peak should not be detected because the current price is too low
    """

    Variable("mail_activated").set(False)
    Variable("sell_activated").set(False)  # test or real
    Variable("coinbase_api_call_activated").set(False)  # test or real

    delete_directory_if_exists("CRYPTO json")

    crypto = Crypto()
    crypto.name = "BTC"
    crypto.coinbaseId = "BTC"
    crypto.current_price = 9
    crypto.amount = 10
    crypto.max_price = 12
    crypto.break_even_point = 101
    crypto.peak_target = 103
    crypto.USDC_balance = 20
    crypto.last_order_buy_price = 9

    crypto.write_variables_to_json_file()

    Variable("TEST_sell_order_done001").set(False)
    ProcessPeakDetection()

    assert Variable("TEST_sell_order_done001").get() == False

    Variable("TEST_sell_order_done001").set(False)

    delete_directory_if_exists("CRYPTO json")










