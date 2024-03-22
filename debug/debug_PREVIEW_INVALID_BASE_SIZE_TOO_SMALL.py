"""
Debug of preview invalid base size too small
"""

import sys
sys.path.append('./')


from functions_crypto import *
import cryptocompare
import time
from functions_email import *
from global_variables import *
from class_cryptos import *
from functions_log import *


# Set up CRYPTOS object
CRYPTOS_object = CRYPTOS()
CRYPTOS_object.getCRYPTO_json()


Variable("mode").set("test")

for c in CRYPTOS_object.cryptos_list:
    
    print(c.name)
    order = c.sell_for_USDC()
    print(order)
