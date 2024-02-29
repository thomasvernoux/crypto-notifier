from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *


CRYPTOS = getCRYPTO()

def crypto_process(crypto):
    print(f"Nom : {crypto.name}, Amount : {crypto.amount}, Prix d'achat : {crypto.buy_price}, Prix maximum : {crypto.max_price}, Current price : {crypto.current_price}")
    crypto.current_price = cryptocompare.get_price(crypto.name, 'USD')[crypto.name]["USD"]
    if crypto.current_price > crypto.max_price :
        crypto.max_price = crypto.current_price
    crypto.USDC_balance = crypto.amount * crypto.current_price
    crypto.profit_percent = crypto.current_price / crypto.buy_price * 100

    if ((0.98 * crypto.current_price) < crypto.max_price) & (crypto.number_of_alert_authorized >= 1):
        # time to sell alert
        subject = "Time to sell alert"
        body = f"{crypto.name} is 0.98% maximum value.\nMax value : {crypto.max_price}\nCurrent value : {crypto.current_price}\nBuy price : {crypto.buy_price}"
        send_email(subject, body)
        crypto.number_of_alert_authorized -= 1
    
    
    
    
    
    
    return crypto

while True :
    for crypto in CRYPTOS:
        crypto = crypto_process(crypto)
        



    writeCRYPTO(CRYPTOS)

    #send_email("crypto check", "test")
    #print("mail send")

    time.sleep(5)
