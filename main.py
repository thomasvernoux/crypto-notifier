"""
Main programm to launch processes
Author : Thomas Vernoux
Date : March 3, 2024
"""

import traceback

from multiprocessing import Pool


from process_price_update import *
from process_update_account import *
from process_peak_detection import *
from process_ctrlC_detector import *


set_variable_time_loop_update_account_process(10)
set_variable_time_loop_update_price_process(3)
set_variable_time_loop_update_price_all_process(6)
set_variable_time_loop_PeakDetection_process(3)

set_variable_coinbase_api_sell_activated(False)
set_variable_coinbase_api_getprice_activated(True)
set_variable_test_mode_activated(False)

set_variable_program_on(True)

set_variable_trace_activated(True)




if __name__ == "__main__":
    
    with Pool() as pool:
        
        try :

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

            print("All processes completed successfully")
            
        except Exception as e:
            tb = traceback.format_exc()
            pool.terminate()
            set_variable_program_on(False)
            print(f"Error occurred: {str(tb)}")
            log_error_critic(tb)


        

    
