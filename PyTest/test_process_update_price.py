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
from process_update_price import *
from functions_basics import *

import shutil


Variable("sell_activated").set(False)  # test or real
Variable("coinbase_api_call_activated").set(False)  # test or real

def test_update_single_crypto():
    """
    A simple test for update_single_crypto function
    """



    Variable("coinbase_api_call_activated").set(True)

    delete_directory_if_exists("CRYPTO json")

    crypto = Crypto()
    crypto.name = "BTC"
    crypto.coinbaseId = "BTC"
    crypto.current_price = 10
    crypto.amount = 10

    update_single_crypto(crypto)

    crypto2 =  Crypto()
    crypto2.name = "BTC"
    crypto2.get_crypto_from_json_file()

    delete_directory_if_exists("CRYPTO json")
    Variable("coinbase_api_call_activated").set(False)

    assert crypto2.amount == crypto.amount
    assert crypto2.current_price != 10
    assert crypto2.max_price != 0
    assert crypto2.USDC_balance != 0







def update_crypto_prices():

    crypto = Crypto()
    crypto.name = "test"

    cryptos_list = [crypto]

    update_crypto_prices(cryptos_list)

    assert get_price(crypto) == 1000



