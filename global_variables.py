
"""
This file contain global variables getters and setters
Author : Thomas Vernoux
Date : March 3, 2024
"""

import json
import os

variables_directory = "global_variables"

def set_variable_json(variable_name, value):
    # Vérifier si le répertoire pour les variables existe, sinon le créer
    if not os.path.exists(variables_directory):
        os.makedirs(variables_directory)

    filename = os.path.join(variables_directory, variable_name + ".json")

    # Écrire la valeur dans le fichier JSON
    with open(filename, 'w') as f:
        json.dump(value, f)

def get_variable_json(variable_name):
    filename = os.path.join(variables_directory, variable_name + ".json")
    try:
        # Charger la valeur à partir du fichier JSON
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print(f"Erreur lors de la récupération de la variable JSON : {variable_name}")
        return None














# mode
def set_variable_mode(nouvelle_valeur):
    set_variable_json("mode", nouvelle_valeur)
    
def get_variable_mode():
    return get_variable_json("mode")

# test_mail_send  -  For test mode : return True if a mail should have been sent in real mode
def set_variable_test_mail_send(nouvelle_valeur):
    set_variable_json("test_mail_send", nouvelle_valeur)

def get_variable_test_mail_send():
    return get_variable_json("test_mail_send")

# dico account Id : vdictionary that associate crypto name to account id
def set_variable_dico_account_id(nouvelle_valeur):
    set_variable_json("dico_account_id", nouvelle_valeur)

def get_variable_dico_account_id():
    return get_variable_json("dico_account_id")

# sound activated
def set_variable_sound_activated(nouvelle_valeur):
    set_variable_json("sound_activated", nouvelle_valeur)

def get_variable_sound_activated():
    return get_variable_json("sound_activated")

# Extern crypto change detected
"""
This variable is a flag when an extern change has been made with crypto
"""

def set_variable_extern_change_detected(nouvelle_valeur):
    set_variable_json("extern_change_detected", nouvelle_valeur)

def get_variable_extern_change_detected():
    return get_variable_json("extern_change_detected")

# Number of recursiv call
"""
This variable is a flag when an extern change has been made with crypto
"""

def set_variable_recursiv_call_number(nouvelle_valeur):
    set_variable_json("recursiv_call_number", nouvelle_valeur)

def get_variable_recursiv_call_number():
    return get_variable_json("recursiv_call_number")

"""
Activate program trace
"""

def set_variable_trace_activated(nouvelle_valeur):
    set_variable_json("trace_activated", nouvelle_valeur)

def get_variable_trace_activated():
    return get_variable_json("trace_activated")

"""
time between loop for update account process
"""

def set_variable_time_loop_update_account_process(nouvelle_valeur):
    set_variable_json("time_loop_update_account_process", nouvelle_valeur)

def get_variable_time_loop_update_account_process():
    return get_variable_json("time_loop_update_account_process")

"""
time between loop for update crypto price process (ALL)
"""

def set_variable_time_loop_update_price_all_process(nouvelle_valeur):
    set_variable_json("time_loop_update_price_all_process", nouvelle_valeur)

def get_variable_time_loop_update_price_all_process():
    return get_variable_json("time_loop_update_price_all_process")

"""
time between loop for update crypto price process
"""

def set_variable_time_loop_update_price_process(nouvelle_valeur):
    set_variable_json("time_loop_update_price_process", nouvelle_valeur)

def get_variable_time_loop_update_price_process():
    return get_variable_json("time_loop_update_price_process")

def set_variable_time_loop_PeakDetection_process(nouvelle_valeur):
    set_variable_json("time_loop_PeakDetection_process", nouvelle_valeur)

def get_variable_time_loop_PeakDetection_process():
    return get_variable_json("time_loop_PeakDetection_process")



    # def error_check(self):

    #     if self.test_mode_activated :
    #         if self.coinbase_api_sell_activated == True : 
    #             print("fatal error, set_run_mode, class run mode - test mode activated and coinbase_api_sell also")
    #         if self.coinbase_api_getprice_activated == True : 
    #             print("fatal error, set_run_mode, class run mode - test mode activated and coinbase_api_getprice also")

def set_variable_coinbase_api_sell_activated(nouvelle_valeur):
    set_variable_json("coinbase_api_sell_activated", nouvelle_valeur)

def get_variable_coinbase_api_sell_activated():
    return get_variable_json("coinbase_api_sell_activated")

def set_variable_coinbase_api_getprice_activated(nouvelle_valeur):
    set_variable_json("coinbase_api_sell_activated", nouvelle_valeur)

def get_variable_coinbase_api_getprice_activated():
    return get_variable_json("coinbase_api_sell_activated")

def set_variable_test_mode_activated(nouvelle_valeur):
    set_variable_json("test_mode_activated", nouvelle_valeur)

def get_variable_test_mode_activated(nouvelle_valeur):
    return get_variable_json("test_mode_activated")




"""
Variable program on
"""

def set_variable_program_on(nouvelle_valeur):
    set_variable_json("program_on", nouvelle_valeur)
    return 

def get_variable_program_on():
    return get_variable_json("program_on")







"""
Variables init
"""



set_variable_trace_activated(False)
set_variable_time_loop_update_account_process(60*5)
set_variable_time_loop_update_price_all_process(60*5)












































