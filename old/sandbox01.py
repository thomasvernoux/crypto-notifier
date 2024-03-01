

from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *
from cryptoprocess import *
from function_history import *



CRYPTOS = getCRYPTO()



while True :
    for crypto in CRYPTOS:
        values = read_last_values_fichier(crypto, 10)
        print(crypto.name, values)
        



    

    time.sleep(10)
