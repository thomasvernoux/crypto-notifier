
"""
Author : Thomas Vernoux
Date : 29/02/2024
This file contain the crypto_process function
"""
from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *
from global_variables import *
from function_history import *




def crypto_process(crypto):
    """
    input and output : crypto (from crypto class)
    The cryptoprocess functoin process a crypto once.
    The function do the following actions : 
    Print the crypto in term, actaulise crypto value
    Notify by email if necessary 
    """
    

    # simple print
    print(f"Nom : {crypto.name_cryptocompare}, Amount : {crypto.amount}, Prix d'achat : {crypto.buy_price}, Prix maximum : {crypto.max_price}, Current price : {crypto.current_price}")
    
    # Price actualisation
    if get_variable_mode() == "real":
        crypto.current_price_cryptocompare = get_price(crypto)
        
    
    # Max price actualisation
    if crypto.current_price > crypto.max_price :
        crypto.max_price = crypto.current_price
    
    # USDC balance actualisation
    crypto.USDC_balance = crypto.amount * crypto.current_price
    crypto.profit_percent = crypto.current_price / crypto.buy_price * 100


    ## peak reset
    if crypto.current_price < crypto.buy_price : 
        crypto.max_price = 0



    ## peak detection
    peak_limit = crypto.peak_target * 100 * crypto.current_price
    if (peak_limit < crypto.max_price) & (crypto.number_of_alert_authorized >= 1) & time_interval(crypto):
        # a peak is detected
        # time to sell alert
        subject = "Time to sell alert"
        body = f"{crypto.name} is {crypto.peak_target}% maximum value.\nMax value : {crypto.max_price}\nCurrent value : {crypto.current_price}\nBuy price : {crypto.buy_price}"
        
        if get_variable_mode() == "real":
            send_email(subject, body)
        elif get_variable_mode() == "test":
            set_variable_test_mail_send(True)
        crypto.number_of_alert_authorized -= 1

        # update last notification time
        crypto.last_notification_time = time.time()

    ## save price history in appropriate file
    save_to_file(crypto)

    
    
    
    return crypto