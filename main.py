"""
Main programm to launch processes
Author : Thomas Vernoux
Date : March 3, 2024
"""

from multiprocessing import Pool


from process_price_update import *
from process_update_account import *
from process_peak_detection import *
from process_ctrlC_detector import *


set_variable_time_loop_update_account_process(10)
set_variable_time_loop_update_price_process(3)
set_variable_time_loop_update_price_all_process(6)
set_variable_time_loop_PeakDetection_process(3)

set_variable_running_mode_coinbase_api_sell_activated(False)
set_variable_running_mode_coinbase_api_getprice_activated(True)
set_variable_running_mode_test_mode_activated(False)

set_variable_program_on(True)




if __name__ == "__main__":
    
    with Pool() as pool:
        

        result1 = pool.apply_async(ProcessUpdatePrice)
        result2 = pool.apply_async(ProcessUpdatePrice_ALL)
        result3 = pool.apply_async(ProcessUpdateAccount)
        result4 = pool.apply_async(ProcessPeakDetection)
        result5 = pool.apply_async(processCTRLcDetector)


        print("All process launched")

        result1.get()
        result2.get()
        result3.get()
        result4.get()
        result5.get()


        

    
