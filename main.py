"""
Main program to launch processes
Author: Thomas Vernoux
Date: March 3, 2024
"""

import traceback
from class_process import *
from process_update_price import *
from process_update_account import *
from process_peak_detection import *
from process_heart_beat import *

if __name__ == "__main__":
    try :
        # Clear global variables
        remove_global_variables()

        # Global variables initialization
        Variable("trace_activated").set(True)

        Variable("mode").set("real")  # test or real
        Variable("sell_activated").set(True)  
        Variable("coinbase_api_call_activated").set(True) 
        Variable("mail_activated").set(True)

        
        Variable("filename_dic").set({})
        Variable("trace_activated").set(True)

        Variable("break_even_point").set(104)

        # Processes creation
        ProcessUpdateAccount   = PROCESS(ProcessUpdateAccount, loop_time_min=60*5)
        ProcessUpdatePrice_ALL = PROCESS(ProcessUpdatePrice_ALL, loop_time_min=60*20)
        ProcessUpdatePrice     = PROCESS(ProcessUpdatePrice, loop_time_min=30)
        ProcessPeakDetection   = PROCESS(ProcessPeakDetection, loop_time_min=30)
        ProcessHeartBeat       = PROCESS(ProcessHeartBeat, loop_time_min=60*60*6)

        # Infinite loop to run processes
        while True:
            ProcessUpdateAccount.loop()
            """
            debug, erreur ici , "last_order_buy_price": null,
            """
            ProcessUpdatePrice_ALL.loop()
            """
            Au dessus
            """
            ProcessUpdatePrice.loop()
            ProcessPeakDetection.loop()
            ProcessHeartBeat.loop()

    except Exception as e:
        tb = traceback.format_exc()
        error_message = f"Error in main program :\n{tb}"
        print(error_message)
        send_email("Error", error_message)
        log_error_critic(error_message)
