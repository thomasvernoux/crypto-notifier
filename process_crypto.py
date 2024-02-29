from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *

time_notif_interval = 10 * 60  # interval between 2 notofications : 10 min


CRYPTOS = getCRYPTO()

def time_interval(crypto):
    if time.time() > crypto.last_notification_time + time_notif_interval:
        return True
    return False

def crypto_process(crypto):
    # simple print
    print(f"Nom : {crypto.name}, Amount : {crypto.amount}, Prix d'achat : {crypto.buy_price}, Prix maximum : {crypto.max_price}, Current price : {crypto.current_price}")
    
    # Price actualisation
    crypto.current_price = cryptocompare.get_price(crypto.name, 'USD')[crypto.name]["USD"]
    
    # Max price actualisation
    if crypto.current_price > crypto.max_price :
        crypto.max_price = crypto.current_price
    
    # USDC balance actualisation
    crypto.USDC_balance = crypto.amount * crypto.current_price
    crypto.profit_percent = crypto.current_price / crypto.buy_price * 100


    ## peak detection
    if ((0.98 * crypto.current_price) < crypto.max_price) & (crypto.number_of_alert_authorized >= 1) & time_interval(crypto):
        # time to sell alert
        subject = "Time to sell alert"
        body = f"{crypto.name} is 0.98% maximum value.\nMax value : {crypto.max_price}\nCurrent value : {crypto.current_price}\nBuy price : {crypto.buy_price}"
        send_email(subject, body)
        crypto.number_of_alert_authorized -= 1

        # update last notification time
        crypto.last_notification_time = time.time()
    
    
    
    
    
    
    return crypto

while True :
    for crypto in CRYPTOS:
        crypto = crypto_process(crypto)
        



    writeCRYPTO(CRYPTOS)

    #send_email("crypto check", "test")
    #print("mail send")

    time.sleep(1)
