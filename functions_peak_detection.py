"""
This file contain the peak detection functions
Author : Thomas Vernoux
Date : March 3, 2024
"""

from functions_crypto import *
import cryptocompare
import time
from functions_email import *
from global_variables import *
from functions_log import *


def peak_detection_O1(crypto):
    """
    Detect crypto price peak using the max value. 
    Detect when the crypto price is under a certain % of the max value
    """

    peak_limit_value = crypto.peak_target / 100 * crypto.max_price
    break_even_value = crypto.buy_price * crypto.break_even_point / 100

    # Simple check
    if crypto.buy_price == None :
        log_error_critic(f"buy price is missing for : {crypto.name}")

    ## percentage of accomplishment for break_even_point 
    pafbep = round(((crypto.current_price - crypto.buy_price) / (break_even_value - crypto.buy_price)) * 100, 1)
    print(f"{crypto.name}  percentage of accomplishment for break_even_point : ", pafbep, "%   -  ", "crypto value/max : ", round(crypto.current_price/crypto.max_price * 100, 2))
    log_write(f"peak detection", f"{crypto.name} - percentage of accomplishment for break_even_point : {pafbep} %\n")

    if crypto.current_price < break_even_value : 
        # cryptocurrency is not profitable
        return False

    """
    DEBUG
    """

    if crypto.name == "RENDER":
        a = 3

    if crypto.current_price > break_even_value :                             
        log_write("peak detection", f"      crypto.current_price > break_even_value : {crypto.name} peak limit value : {peak_limit_value}, break even value : {break_even_value}" )
        if (crypto.current_price < peak_limit_value):                                     # on est sur la phase descendante du pic
            log_write("peak detection", f"  crypto.current_price < peak_limit : {crypto.name}, peak limit : {peak_limit_value}" )
            
            log_write("peak detection", "Peak detected : " + crypto.get_crypto_info_str() )
            return True
            
        
    
    
    if crypto.current_price < peak_limit_value * 0.99 : 
        # sell missed
        print(f"peak missed : {crypto.name}")
        log_write("peak detection", f"peak missed : {crypto.name}")

    
    
    return False
                