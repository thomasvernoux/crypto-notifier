"""
Date : 2024 march 18
Author : Thomas Vernoux
Description : 
This file contain the peak detection process

"""



import time

from functions_crypto import *
from functions_email import *
from functions_specials_alerts import *
from functions_log import *
from class_cryptos import *
from functions_basics import *

import inspect



def ProcessPeakDetection():
    """
    Peak detection process
    """

    

    try:

        # reset Variable : heartbeat_message
        Variable("heartbeat_message").set("")

        log_write("working process", "ProcessPeakDetection")
        
        CRYPTOS_object = CRYPTOS()
        CRYPTOS_object.getCRYPTO_json()
        
        for i in range (len(CRYPTOS_object.cryptos_list)):
            """
            DEBUG
            """
            if CRYPTOS_object.cryptos_list[i].name == "ADA":
                a = 3

            if CRYPTOS_object.cryptos_list[i].USDC_balance < 0.5 :
                continue
            """
            Error check
            """
            if not(crypto_check_peak_detection(CRYPTOS_object.cryptos_list[i])):
                continue
            """
            end of Error check 
            """

            peak_detection = False
            try : 
                peak_detection = peak_detection_O1(CRYPTOS_object.cryptos_list[i])
            except Exception as e:
                print("Error with peak detection")
                tb = traceback.format_exc()
                print(tb)
                log_error_critic(tb)

            if peak_detection :
                # peak detected, the crypto has to be sold

                if Variable("mode").get() == "test":
                    # if test mode, set the mail flag to True
                    Variable("test_mail_send").set(True)
                    return True
                
                elif Variable("mode").get() == "real":
                    # Sell crypto
                    try :
                        order = CRYPTOS_object.cryptos_list[i].sell_for_USDC()
                        send_email("Sell order done", str(order))
                        CRYPTOS_object.cryptos_list[i].max_price = 0
                        CRYPTOS_object.cryptos_list[i].last_order_buy_price = 0
                        CRYPTOS_object.cryptos_list[i].amount = 0
                        CRYPTOS_object.cryptos_list[i].USDC_balance = 0
                        Variable("extern_change_detected").set(True)
                        CRYPTOS_object.cryptos_list[i].write_variables_to_json_file()

                    except Exception as e : 
                        tb = traceback.format_exc()
                        print(f"Error while trying to sell crypto : {CRYPTOS_object.cryptos_list[i].name}")
                        log_error_minor(f"Error while trying to sell crypto : {CRYPTOS_object.cryptos_list[i].name}. Traceback : {tb}")




    except KeyboardInterrupt:
        print("End of ProcessPeakDetection")

