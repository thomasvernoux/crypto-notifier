



from functions_crypto import *
import cryptocompare
import time
from functions_email import *
from cryptoprocess import *
from specials_alerts import *



CRYPTOS = getCRYPTO()

set_variable_mode("real")                  # real  / test  mode

while True :
    
    specials_alerts(CRYPTOS)

    time.sleep(60 * 5)


"""
Is CoinGecko API free?
CoinGecko API offers both free and paid plans. 
The Demo API plan is accessible to all CoinGecko users at zero cost, 
with a stable rate limit of 30 calls/min and a monthly cap of 10,000 calls.

= 13 calls per hours
"""


