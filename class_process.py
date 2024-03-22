"""
A simple classe to manage processes
Author : Thomas Vernoux
Date : march 22, 2024
"""



from typing import Callable
import time


class PROCESS:
    def __init__(self, process_function : Callable, loop_time_min = 0):
        self.process_function = process_function
        self.loop_time_min = loop_time_min
        self.loop_time_max = None
        self.loop_time_measured = None

        self.last_loop_date = None

    def loop(self):
        if self.trig():
            self.process_function()

    def trig(self):
        
        Time = time.time()
        if self.last_loop_date == None : 
            self.last_loop_date = Time
            return True
        

        if self.last_loop_date + self.loop_time_min < Time :
            return True
        
        return False


