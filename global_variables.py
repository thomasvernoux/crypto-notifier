
"""
This file contain global variables getters and setters
Author : Thomas Vernoux
Date : March 3, 2024
"""

import json
import os

filename_global_variables = "global_variables.json"

def set_get_variable_json(variable_name, value):
    
    if not os.path.exists(filename_global_variables):
        with open(filename_global_variables, 'w') as f:
            json.dump({}, f)  # Créez un fichier JSON vide si le fichier n'existe pas encore
    
    try:
        # Charger les valeurs actuelles du fichier JSON
        with open(filename_global_variables, 'r') as f:
            variables = json.load(f)
    except FileNotFoundError:
        variables = {}

    # Définir la valeur de la variable dans le dictionnaire
    variables[variable_name] = value

    # Écrire les valeurs mises à jour dans le fichier JSON
    with open(filename_global_variables, 'w') as f:
        json.dump(variables, f)

def get_variable_json(variable_name):
    try:
        # Charger les valeurs actuelles du fichier JSON
        with open(filename_global_variables, 'r') as f:
            variables = json.load(f)
            # Récupérer la valeur de la variable
            return variables.get(variable_name)
    except FileNotFoundError:
        # Si le fichier n'existe pas, retourner None
        return None














# mode
def set_variable_mode(nouvelle_valeur):
    set_get_variable_json("mode", nouvelle_valeur)
    
def get_variable_mode():
    return get_variable_json("mode")

# test_mail_send  -  For test mode : return True if a mail should have been sent in real mode
def set_variable_test_mail_send(nouvelle_valeur):
    set_get_variable_json("test_mail_send", nouvelle_valeur)

def get_variable_test_mail_send():
    return get_variable_json("test_mail_send")

# dico account Id : vdictionary that associate crypto name to account id
def set_variable_dico_account_id(nouvelle_valeur):
    set_get_variable_json("dico_account_id", nouvelle_valeur)

def get_variable_dico_account_id():
    return get_variable_json("dico_account_id")

# sound activated
def set_variable_sound_activated(nouvelle_valeur):
    set_get_variable_json("sound_activated", nouvelle_valeur)

def get_variable_sound_activated():
    return get_variable_json("sound_activated")

# Extern crypto change detected
"""
This variable is a flag when an extern change has been made with crypto
"""

def set_variable_extern_change_detected(nouvelle_valeur):
    set_get_variable_json("extern_change_detected", nouvelle_valeur)

def get_variable_extern_change_detected():
    return get_variable_json("extern_change_detected")

# Number of recursiv call
"""
This variable is a flag when an extern change has been made with crypto
"""

def set_variable_recursiv_call_number(nouvelle_valeur):
    set_get_variable_json("recursiv_call_number", nouvelle_valeur)

def get_variable_recursiv_call_number():
    return get_variable_json("recursiv_call_number")

"""
Activate program trace
"""

def set_variable_trace_activated(nouvelle_valeur):
    set_get_variable_json("trace_activated", nouvelle_valeur)

def get_variable_trace_activated():
    return get_variable_json("trace_activated")

"""
time between loop for update account process
"""

def set_variable_time_loop_update_account_process(nouvelle_valeur):
    set_get_variable_json("time_loop_update_account_process", nouvelle_valeur)

def get_variable_time_loop_update_account_process():
    return get_variable_json("time_loop_update_account_process")

"""
time between loop for update crypto price process (ALL)
"""

def set_variable_time_loop_update_price_all_process(nouvelle_valeur):
    set_get_variable_json("time_loop_update_price_all_process", nouvelle_valeur)

def get_variable_time_loop_update_price_all_process():
    return get_variable_json("time_loop_update_price_all_process")

"""
time between loop for update crypto price process
"""

def set_variable_time_loop_update_price_process(nouvelle_valeur):
    set_get_variable_json("time_loop_update_price_process", nouvelle_valeur)

def get_variable_time_loop_update_price_process():
    return get_variable_json("time_loop_update_price_process")

def set_variable_time_loop_PeakDetection_process(nouvelle_valeur):
    set_get_variable_json("time_loop_PeakDetection_process", nouvelle_valeur)

def get_variable_time_loop_PeakDetection_process():
    return get_variable_json("time_loop_PeakDetection_process")

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
    run_mode_instance.coinbase_api_sell_activated = nouvelle_valeur
    run_mode_instance.error_check()
    set_get_variable_json("run_mode_instance", nouvelle_valeur)
    return

def set_variable_running_mode_coinbase_api_getprice_activated(nouvelle_valeur):
    run_mode_instance.coinbase_api_getprice_activated = nouvelle_valeur
    run_mode_instance.error_check()
    set_get_variable_json("run_mode_instance", nouvelle_valeur)
    return

def set_variable_running_mode_test_mode_activated(nouvelle_valeur):
    run_mode_instance.test_mode_activated = nouvelle_valeur
    run_mode_instance.error_check()
    set_get_variable_json("run_mode_instance", nouvelle_valeur)
    return 

def get_variable_run_mode():
    return get_variable_json("run_mode_instance")


"""
Variable program on
"""

def set_variable_program_on(nouvelle_valeur):
    set_get_variable_json("program_on", nouvelle_valeur)
    return 

def get_variable_program_on():
    return get_variable_json("program_on")







"""
Variables init
"""
set_variable_trace_activated(False)
set_variable_time_loop_update_account_process(60*5)
set_variable_time_loop_update_price_all_process(60*5)
run_mode_instance = RUN_MODE()











































