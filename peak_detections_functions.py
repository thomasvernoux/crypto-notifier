

from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *
from global_variables import *
from function_history import *
from log import *


def peak_detection_O1(crypto):
    """
    Detect crypto price peak using the max value. 
    Detect when the crypto price is under a certain % of the max value
    """

    if crypto.name == "SHIB":
        print("a")

    #print("peak detection for : ", crypto.name)
    write_log("peak detection", f"peak detection for :  {crypto.name}")

    peak_limit_value = crypto.peak_target / 100 * crypto.max_price
    break_even_value = crypto.buy_price * crypto.break_even_point / 100

    if crypto.current_price > break_even_value :                             
        write_log("peak detection", f"      crypto.current_price > break_even_value : {crypto.name}" )
        if (crypto.current_price < peak_limit_value):                                     # on est sur la phase descendante du pic
            write_log("peak detection", f"  crypto.current_price < peak_limit : {crypto.name}, peak limit : {peak_limit_value}" )
            if (crypto.number_of_alert_authorized >= 1) & (time_interval(crypto)):  # on evite de trop notifier
                write_log("peak detection", "Peak detected : " + crypto.get_crypto_info_str() )
                return True
        
    
    
    if crypto.current_price < peak_limit_value * 0.99 : 
        # sell missed
        print(f"peak missed : {crypto.name}")
        write_log("peak detection", f"peak missed : {crypto.name}")

    ## percentage of accomplishment for break_even_point
    pafbep = round(((crypto.current_price - crypto.buy_price) / (break_even_value - crypto.buy_price)) * 100, 1)
    print(f"{crypto.name}  percentage of accomplishment for break_even_point : ", pafbep, "%   -  ", "crypto value/max : ", round(crypto.current_price/crypto.max_price * 100, 2))
    write_log(f"peak detection", f"{crypto.name} - percentage of accomplishment for break_even_point : {pafbep} %\n")
    
    return False
                