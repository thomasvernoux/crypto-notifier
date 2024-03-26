"""
Main program to launch processes
Author: Thomas Vernoux
Date: March 3, 2024
"""

import traceback
from class_process import *
from process_price_update import *
from process_update_account import *
from process_peak_detection import *

if __name__ == "__main__":
    # Clear global variables
    remove_global_variables()

    # Global variables initialization
    Variable("trace_activated").set(True)

    Variable("mode").set("test")  # test or real
    Variable("filename_dic").set({})
    Variable("trace_activated").set(True)

    # Processes creation
    ProcessUpdateAccount = PROCESS(ProcessUpdateAccount, loop_time_min=60*5)
    ProcessUpdatePrice_ALL = PROCESS(ProcessUpdatePrice_ALL, loop_time_min=60*20)
    ProcessUpdatePrice = PROCESS(ProcessUpdatePrice, loop_time_min=30)
    ProcessPeakDetection = PROCESS(ProcessPeakDetection, loop_time_min=30)

    # Infinite loop to run processes
    while True:
        ProcessUpdateAccount.loop()
        ProcessUpdatePrice_ALL.loop()
        ProcessUpdatePrice.loop()
        ProcessPeakDetection.loop()
