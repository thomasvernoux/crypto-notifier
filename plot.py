from functions_plot import *
from class_cryptos import *


CRYPTOS_object = CRYPTOS()
CRYPTOS_object.getCRYPTO_json()



for crypto in CRYPTOS_object.cryptos_list :
    crypto_name = crypto.name

    if crypto.USDC_balance > 0.5 :
        try : 
            plot_crypto(crypto_name = crypto_name)
        except : 
            None