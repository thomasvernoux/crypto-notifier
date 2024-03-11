
from fonctions_crypto import *
import cryptocompare
import time

from send_email_file import *

from specials_alerts import *
from class_crypos import *

from log import *



# Set up CRYPTOS object
CRYPTOS_object = CRYPTOS()
CRYPTOS_object.getCRYPTO_json()




        

print(CRYPTOS_object.cryptos_list)

for crypto in CRYPTOS_object.cryptos_list:    
    crypto.write_variables_to_json_file()







