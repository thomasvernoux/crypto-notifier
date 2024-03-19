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








if __name__ == "__main__":


    remove_global_variables()
    global_variables_init()

    Variable("time_loop_update_account_process").set(10)
    Variable("time_loop_update_price_process").set(3)
    Variable("time_loop_update_price_all_process").set(6)
    Variable("time_loop_PeakDetection_process").set(3)

    Variable("coinbase_api_sell_activated").set(False)
    Variable("coinbase_api_getprice_activated").set(True)
    Variable("test_mode_activated").set(False)

    Variable("program_on").set(True)

    Variable("trace_activated").set(True)

    Variable("recursiv_call_number").set(0)
    
    with Pool() as pool:
        
        try :

            result5 = pool.apply_async(processCTRLcDetector)
            result3 = pool.apply_async(ProcessUpdateAccount)
            time.sleep(5)
            result2 = pool.apply_async(ProcessUpdatePrice_ALL)
            time.sleep(5)

            result1 = pool.apply_async(ProcessUpdatePrice)
            result4 = pool.apply_async(ProcessPeakDetection)
            

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
            Variable("program_on").set(False)
            print(f"Error occurred: {str(tb)}")
            log_error_critic(tb)


        

    
