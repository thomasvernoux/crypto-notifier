

import sys
sys.path.append('./')

from class_cryptos import *


def test_sell_for_USDC():
    set_variable_mode("test")
    crypto = Crypto()
    crypto.name = "AUCTION"
    order = crypto.sell_for_USDC()
    print(order)

    return 



test_sell_for_USDC()

