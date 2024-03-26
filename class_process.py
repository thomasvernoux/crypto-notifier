"""
A simple class to manage processes
Author: Thomas Vernoux
Date: March 22, 2024
"""

from typing import Callable
import time
from functions_log import *


class PROCESS:
    """
    A class representing a process handler.
    It manages the execution of a given process function at defined time intervals.
    """

    def __init__(self, process_function: Callable, loop_time_min=0):
        """
        Initialize a PROCESS instance.

        Args:
            process_function (Callable): The function to be executed as the process.
            loop_time_min (int, optional): The minimum time interval between successive process executions, in minutes. Defaults to 0.
        """
        self.process_function = process_function  # The function to be executed
        self.process_function_name = process_function.__name__  # Name of the process function
        self.loop_time_min = loop_time_min  # Minimum time interval between process executions
        self.loop_time_max = None  # Maximum time interval between process executions
        self.loop_time_measured = None  # Measured time interval between process executions

        self.last_loop_date = None  # Timestamp of the last process execution

        self.loop_start_time = None  # Timestamp of the current process execution start
        self.loop_stop_time = None  # Timestamp of the current process execution end
        self.process_time = None  # Time taken for the process execution

    def loop(self):
        """
        Execute the process function if the time condition is met.
        """
        if self.trig():
            print(f"{self.process_function_name} - Start loop :  {time.strftime('%a %b %d %Y - %H:%M:%S')}")
            self.loop_start_time = time.time()
            self.process_function()  # Execute the process function
            self.loop_stop_time = time.time()
            self.process_time = self.get_process_time()  # Calculate process execution time

            loop_time_message = f"Process time : {self.process_function.__name__}     {self.process_time}"
            print(loop_time_message)
            log_write("process_loop_time", loop_time_message)  # Log process execution time

    def trig(self):
        """
        Check if the time condition for process execution is met.

        Returns:
            bool: True if the time condition is met, False otherwise.
        """
        Time = time.time()  # Current timestamp
        if self.last_loop_date is None:
            self.last_loop_date = Time
            return True

        if self.last_loop_date + self.loop_time_min < Time:
            self.last_loop_date = Time
            return True

        return False

    def get_process_time(self):
        """
        Calculate the time taken for the process execution.

        Returns:
            float: Time taken for the process execution.
        """
        return round(self.loop_stop_time - self.loop_start_time, 3)
