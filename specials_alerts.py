
from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *
from global_variables import *
from function_history import *
from peak_detections_functions import *

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


