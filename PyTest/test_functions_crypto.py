"""
Date : 2024/05/13
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
from class_cryptos import *


Variable("sell_activated").set(False)  # test or real
Variable("coinbase_api_call_activated").set(False)  # test or real



def test_get_price():

    crypto = Crypto()
    crypto.name = "test"

    assert get_price(crypto) == 1000



