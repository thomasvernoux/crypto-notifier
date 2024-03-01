

from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *
from cryptoprocess import *
from global_variables import *
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()



def get_crypto_price_coingecko(crypto):
    return cg.get_price(ids=crypto.name_coingecko, vs_currencies='usd')[crypto.name_coingecko]["usd"]

crypto1 = Crypto()
crypto1.name = "Test01"
crypto1.name_coingecko = "pangolin"
crypto1.amount = 8                 
crypto1.buy_price = 1               
crypto1.max_price = 10                 
crypto1.current_price = 8             
crypto1.USDC_balance = 1             
crypto1.number_of_alert_authorized = 1  
crypto1.last_notification_time = 0       
crypto1.peak_target = 80                  


print(get_crypto_price_coingecko(crypto1))
