"""
A simple classe to manage processes
Author : Thomas Vernoux
Date : march 22, 2024
"""



from typing import Callable
import time
from functions_log import *


class PROCESS:
    def __init__(self, process_function : Callable, loop_time_min = 0):
        self.process_function = process_function
        self.loop_time_min = loop_time_min
        self.loop_time_max = None
        self.loop_time_measured = None

        self.last_loop_date = None


        self.loop_start_time = None
        self.loop_stop_time = None
        self.process_time = None

    def loop(self):
        if self.trig():
            self.loop_start_time = time.time()
            self.process_function()
            self.loop_stop_time = time.time()
            self.process_time = self.get_process_time()

            loop_time_message = f"Process time : {self.process_function.__name__}     {self.process_time}"
            print(loop_time_message)
            log_write("process_loop_time", loop_time_message)

    def trig(self):
        
        Time = time.time()
        if self.last_loop_date == None :
            self.last_loop_date = Time 
            return True
        
        if self.last_loop_date + self.loop_time_min < Time :
            self.last_loop_date = Time
            return True
        
        return False
    
    def get_process_time(self):
        return round(self.loop_stop_time - self.loop_start_time, 3)


