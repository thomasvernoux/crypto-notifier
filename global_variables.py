
"""
This file contain global variables getters and setters
Author : Thomas Vernoux
Date : March 3, 2024
"""

# mode
def set_variable_mode(nouvelle_valeur):
    global mode
    mode = nouvelle_valeur
    
def get_variable_mode():
    return mode

# test_mail_send  -  For test mode : return True if a mail should have been sent in real mode
def set_variable_test_mail_send(nouvelle_valeur):
    global test_mail_send
    test_mail_send = nouvelle_valeur

def get_variable_test_mail_send():
    return test_mail_send

# dico account Id : vdictionary that associate crypto name to account id
def set_variable_dico_account_id(nouvelle_valeur):
    global dico_account_id
    dico_account_id = nouvelle_valeur

def get_variable_dico_account_id():
    return dico_account_id

# sound activated
def set_variable_sound_activated(nouvelle_valeur):
    global sound_activated
    sound_activated = nouvelle_valeur

def get_variable_sound_activated():
    return sound_activated

# Extern crypto change detected
"""
This variable is a flag when an extern change has been made with crypto
"""

def set_variable_extern_change_detected(nouvelle_valeur):
    global extern_change_detected
    extern_change_detected = nouvelle_valeur

def get_variable_extern_change_detected():
    return extern_change_detected

# Number of recursiv call
"""
This variable is a flag when an extern change has been made with crypto
"""

def set_variable_recursiv_call_number(nouvelle_valeur):
    global recursiv_call_number
    recursiv_call_number = nouvelle_valeur

def get_variable_recursiv_call_number():
    return recursiv_call_number

"""
Activate program trace
"""

def set_variable_trace_activated(nouvelle_valeur):
    global trace_activated
    trace_activated = nouvelle_valeur

def get_variable_trace_activated():
    return trace_activated

"""
time between loop for update account process
"""

def set_variable_time_loop_update_account_process(nouvelle_valeur):
    global time_loop_update_account_process
    time_loop_update_account_process = nouvelle_valeur

def get_variable_time_loop_update_account_process():
    return time_loop_update_account_process

"""
time between loop for update crypto price process (ALL)
"""

def set_variable_time_loop_update_price_all_process(nouvelle_valeur):
    global time_loop_update_price_all_process
    time_loop_update_price_all_process = nouvelle_valeur

def get_variable_time_loop_update_price_all_process():
    return time_loop_update_price_all_process

"""
time between loop for update crypto price process
"""

def set_variable_time_loop_update_price_process(nouvelle_valeur):
    global time_loop_update_price_process
    time_loop_update_price_process = nouvelle_valeur

def get_variable_time_loop_update_price_process():
    return time_loop_update_price_all_process

def set_variable_time_loop_PeakDetection_process(nouvelle_valeur):
    global time_loop_PeakDetection_process
    time_loop_PeakDetection_process = nouvelle_valeur

def get_variable_time_loop_PeakDetection_process():
    return time_loop_PeakDetection_process

class RUN_MODE:
    """
    Define running mode
    """
    def __init__(self):
        self.coinbase_api_sell_activated = False
        self.coinbase_api_getprice_activated = False
        self.test_mode_activated = False

    def error_check(self):

        if self.test_mode_activated :
            if self.coinbase_api_sell_activated == True : 
                print("fatal error, set_run_mode, class run mode - test mode activated and coinbase_api_sell also")
            if self.coinbase_api_getprice_activated == True : 
                print("fatal error, set_run_mode, class run mode - test mode activated and coinbase_api_getprice also")

def set_variable_running_mode_coinbase_api_sell_activated(nouvelle_valeur):
    global run_mode_instance
    run_mode_instance.coinbase_api_sell_activated = nouvelle_valeur
    run_mode_instance.error_check()
    return

def set_variable_running_mode_coinbase_api_getprice_activated(nouvelle_valeur):
    global run_mode_instance
    run_mode_instance.coinbase_api_getprice_activated = nouvelle_valeur
    run_mode_instance.error_check()
    return

def set_variable_running_mode_test_mode_activated(nouvelle_valeur):
    global run_mode_instance
    run_mode_instance.test_mode_activated = nouvelle_valeur
    run_mode_instance.error_check()
    return 

def get_variable_run_mode():
    global run_mode_instance
    return run_mode_instance

def set_variable_program_on(nouvelle_valeur):
    global program_on
    program_on = nouvelle_valeur
    return 

def get_variable_program_on():
    global program_on
    return program_on







"""
Variables init
"""
set_variable_trace_activated(False)
set_variable_time_loop_update_account_process(60*5)
set_variable_time_loop_update_price_all_process(60*5)
run_mode_instance = RUN_MODE()











































