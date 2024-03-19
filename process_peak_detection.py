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
        while get_variable_program_on():
            print("ProcessPeakDetection loop")
            
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
                    set_variable_program_on(False)
                    tb = traceback.format_exc()
                    print(tb)
                    log_error_critic(e)

                if peak_detection :
                    # peak detected, the crypto has to be sold

                    if get_variable_run_mode().test_mode_activated :
                        # if test mode, set the mail flag to True
                        set_variable_test_mail_send(True)
                        return True
                    
                    elif get_variable_run_mode().coinbase_api_sell_activated:
                        # Sell crypto
                        try :
                            order = CRYPTOS_object.cryptos_list[i].sell_for_USDC()
                            send_email("Sell order done", str(order))
                            CRYPTOS_object.cryptos_list[i].max_price = 0
                            CRYPTOS_object.cryptos_list[i].buy_price = 0
                            CRYPTOS_object.cryptos_list[i].amount = 0
                            CRYPTOS_object.cryptos_list[i].USDC_balance = 0
                            set_variable_extern_change_detected(True)
                            CRYPTOS_object.cryptos_list[i].write_variables_to_json_file()

                        except Exception as e : 
                            print(f"Error while trying to sell crypto : {CRYPTOS_object.cryptos_list[i].name}")
                            log_error_minor(f"Error while trying to sell crypto : {CRYPTOS_object.cryptos_list[i].name}. Traceback : {e}")



            time.sleep(get_variable_time_loop_PeakDetection_process())


    except KeyboardInterrupt:
        set_variable_program_on(False)
        print("End of ProcessPeakDetection")

