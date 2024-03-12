
"""
Special alerts function
This file contain functions for special kind of alerts
Author : Thomas Vernoux
Date : March 3, 2024

"""
from functions_crypto import *
import cryptocompare
import time
from functions_email import *
from global_variables import *
from functions_peak_detection import *

def specials_alerts(CRYPTOS) :
    """
    Specials alerts for some cryptos at a certain value
    """
    for crypto in CRYPTOS : 
        if (crypto.name == "AUCTION") & (crypto.buy_price < crypto.current_price) : 
            
            subject = "Special alert"
            body = f"{crypto.name} : \nCurrent value : {crypto.current_price}\nBuy price : {crypto.buy_price}"
            send_email(subject, body)
        
        if (crypto.name == "PNG") & (crypto.buy_price < crypto.current_price) : 
            
            subject = "Special alert"
            body = f"{crypto.name} : \nCurrent value : {crypto.current_price}\nBuy price : {crypto.buy_price}"
            send_email(subject, body)

        if (crypto.name == "FOX") & (crypto.buy_price < crypto.current_price) : 
            
            subject = "Special alert"
            body = f"{crypto.name} : \nCurrent value : {crypto.current_price}\nBuy price : {crypto.buy_price}"
            send_email(subject, body)

        if (crypto.name == "NCT") & (crypto.buy_price < crypto.current_price) : 
            
            subject = "Special alert"
            body = f"{crypto.name} : \nCurrent value : {crypto.current_price}\nBuy price : {crypto.buy_price}"
            send_email(subject, body)

        if (crypto.name == "PRQ") & (crypto.buy_price < crypto.current_price) : 
            
            subject = "Special alert"
            body = f"{crypto.name} : \nCurrent value : {crypto.current_price}\nBuy price : {crypto.buy_price}"
            send_email(subject, body)


