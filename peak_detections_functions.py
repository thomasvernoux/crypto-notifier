

from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *
from global_variables import *
from function_history import *


def peak_detection_O1(crypto):


    peak_limit = crypto.peak_target * 100 * crypto.max_price
    if crypto.current_price > crypto.buy_price * 1.05 :                             # La crypto à pris 5 %
        if (crypto.current_price < peak_limit):                                     # on est sur la phase descendante du pic
            if (crypto.number_of_alert_authorized >= 1) & (time_interval(crypto)):  # on evite de trop notifier
                return True
    
    return False
                