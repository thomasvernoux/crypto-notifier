"""
Main program to launch processes
Author: Thomas Vernoux
Date: March 3, 2024
"""
import sys
sys.path.append('./')


import traceback
from class_process import *
from process_update_price import *
from process_update_account import *
from process_peak_detection import *
from process_heart_beat import *

if __name__ == "__main__":
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))

    # Clear global variables
    remove_global_variables()

    # Global variables initialization
    Variable("trace_activated").set(True)

    Variable("mode").set("real")  # test or real
    
    Variable("filename_dic").set({})
    Variable("trace_activated").set(True)

    Variable("break_even_point").set(104)

    # Processes creation
    ProcessUpdateAccount   = PROCESS(ProcessUpdateAccount, loop_time_min=60*5)
    ProcessUpdatePrice_ALL = PROCESS(ProcessUpdatePrice_ALL, loop_time_min=60*20)
    ProcessPeakDetection   = PROCESS(ProcessPeakDetection, loop_time_min=30)
    ProcessHeartBeat       = PROCESS(ProcessHeartBeat, loop_time_min=60*60*6)


    # Infinite loop to run processes
    while True:
        ProcessUpdateAccount.loop()
        ProcessUpdatePrice_ALL.loop()
        ProcessPeakDetection.loop()
        ProcessHeartBeat.loop()

        
        


   