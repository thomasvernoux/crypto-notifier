"""
Debug market order sell
"""

"""
Base size : C'est la quantité de la crypto-monnaie de base dans une paire de trading. 
Par exemple, dans la paire BTC/USD, la base size serait la quantité de Bitcoin (BTC) échangée.

Quote size : C'est la quantité de la crypto-monnaie cotée dans une paire de trading. 
Dans la paire BTC/USD, la quote size serait la quantité de dollars américains (USD) échangée.
"""



import time

import sys
sys.path.append('./')

from class_cryptos import *
from functions_basics import *



Variable("mode").set("real")
crypto = Crypto()

# work fine
#crypto.name = "LCX"
#crypto.name = "ASM"


crypto.name = "VARA"


crypto.sell_for_USDC()


