
"""
Author : Thomas Vernoux
Date : 29/02/2024
This file contain the crypto_process function
"""
from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *


def crypto_process(crypto):
    """
    input and output : crypto (from crypto class)
    The cryptoprocess functoin process a crypto once.
    The function do the following actions : 
Pprint the crypto in term, actaulise crypto value
    Notify by email if necessary 
    """
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
    if ((crypto.peak_target / 100 * crypto.current_price) < crypto.max_price) & (crypto.number_of_alert_authorized >= 1) & time_interval(crypto):
        # time to sell alert
        subject = "Time to sell alert"
        body = f"{crypto.name} is {crypto.peak_target}% maximum value.\nMax value : {crypto.max_price}\nCurrent value : {crypto.current_price}\nBuy price : {crypto.buy_price}"
        send_email(subject, body)
        crypto.number_of_alert_authorized -= 1

        # update last notification time
        crypto.last_notification_time = time.time()
    
    
    
    
    
    
    return crypto