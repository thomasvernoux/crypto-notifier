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

    time.sleep(10)
