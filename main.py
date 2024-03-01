from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *
from cryptoprocess import *



CRYPTOS = getCRYPTO()

set_variable_mode("real")                  # real  / test  mode

while True :
    for crypto in CRYPTOS:
        crypto = crypto_process(crypto)
        



    writeCRYPTO(CRYPTOS)
    writeCRYPTO_userfriendly(CRYPTOS)

    #send_email("crypto check", "test")
    #print("mail send")

    time.sleep(60 * 5)


"""
Is CoinGecko API free?
CoinGecko API offers both free and paid plans. 
The Demo API plan is accessible to all CoinGecko users at zero cost, 
with a stable rate limit of 30 calls/min and a monthly cap of 10,000 calls.

= 13 calls per hours
"""


