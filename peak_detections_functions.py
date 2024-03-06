

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

    peak_limit = crypto.peak_target / 100 * crypto.max_price
    if crypto.current_price > crypto.buy_price * crypto.break_even_point / 100 :                             # La crypto à pris 5 %
        if (crypto.current_price < peak_limit):                                     # on est sur la phase descendante du pic
            if (crypto.number_of_alert_authorized >= 1) & (time_interval(crypto)):  # on evite de trop notifier
                write_log("Peak detected : " )   # TODO finish
                return True
    
    return False
                