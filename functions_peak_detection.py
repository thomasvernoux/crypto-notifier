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

from class_cryptos import *

import inspect



def crypto_check_peak_detection(crypto):
    """
    Check crypto variable to prevent errors while peak detection
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))

    # Variables that cannot be null for peak detection
    no_null_variable = [crypto.name, 
                        crypto.amount, 
                        crypto.last_order_buy_price,
                        crypto.break_even_point,
                        crypto.current_price,
                        crypto.coinbaseId,
                        crypto.max_price,
                        crypto.peak_target
                        ]

    # Values that are considered as null
    null_values = [0, -1, None]

    for paramater in no_null_variable :
        if paramater in null_values:
            message = (
                f"critical error detected in crypto_check_peak_detection : {crypto.get_crypto_info_str()}\n"
                "The following parameters cannot be in null_values = [0, -1, None] :\n"
                f"crypto.name, \n"
                f"crypto.amount, \n"
                f"crypto.last_order_buy_price,\n"
                f"crypto.break_even_point,\n"
                f"crypto.current_price,\n"
                f"crypto.coinbaseId,\n"
                f"crypto.max_price,\n"
                f"crypto.peak_target\n")
            print(message)
            log_error_critic(message)
            return False

    return True

    










def peak_detection_O1(crypto):
    """
    Detect crypto price peak using the max value. 
    Detect when the crypto price is under a certain % of the max value
    """

    """
    DEBUG
    """
    if crypto.name == "RBN":
        a = 3

    if crypto.peak_target == 0:
        log_error_critic(f"crypto.peak_target == 0 : {crypto.name}")
        return False
    if crypto.break_even_point == 0:
        log_error_critic(f"crypto.break_even_point == 0 : {crypto.name}")
        return False

    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    peak_limit_value = crypto.peak_target / 100 * crypto.max_price
    break_even_value = crypto.last_order_buy_price * crypto.break_even_point / 100

    # Simple check
    if crypto.last_order_buy_price == None :
        log_error_critic(f"buy price is missing for : {crypto.name}")

    ## percentage of accomplishment for break_even_point
    pafbep = round(((crypto.current_price - crypto.last_order_buy_price) / (break_even_value - crypto.last_order_buy_price)) * 100, 1)
    message = {}
    message["name"] = crypto.name
    message["percentage of accomplishment for break_even_point"] = pafbep
    message["crypto value/max"] = round(crypto.current_price/crypto.max_price * 100, 2)
    message["Buy order datetime"] = crypto.last_order_buy_datetime
    print(message)
    log_write(f"peak detection", str(message))

    # write info to heartbeat message
    Variable("heartbeat_message").add(crypto.name, message)
    

    if crypto.current_price < break_even_value : 
        # cryptocurrency is not profitable
        return False


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
                