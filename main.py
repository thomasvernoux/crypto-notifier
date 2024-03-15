"""
Main programm to launch processes
Author : Thomas Vernoux
Date : March 3, 2024
"""

from multiprocessing import Pool


from process_price_update import *
from process_update_account import *


set_variable_time_loop_update_account_process(10)
set_variable_time_loop_update_price_process(3)
set_variable_time_loop_update_price_all_process(6)


if __name__ == "__main__":
    
    with Pool() as pool:
        

        result1 = pool.apply_async(ProcessUpdatePrice)
        result2 = pool.apply_async(ProcessUpdatePrice_ALL)
        result3 = pool.apply_async(ProcessUpdateAccount)


        print("All process launched")

        result1.get()
        result2.get()
        result3.get()


        

    
