
"""
This file contain global variables getters and setters
Author : Thomas Vernoux
Date : March 3, 2024
"""

import json
import os
import shutil
import time
import traceback

from global_variables_lock_manager import *



variables_directory = "global_variables"


class Variable:
    def __init__(self, name : str):
        """
        Simple class to set and get variable through json file
        """
        self.name = name
        self.variables_directory = "global_variables"


    def set(self, value):
        """
        Set the variable
        """
        # Vérifier si le répertoire pour les variables existe, sinon le créer
        if not os.path.exists(self.variables_directory):
            os.makedirs(self.variables_directory)

        filename = os.path.join(self.variables_directory, self.name + ".json")

        # Écrire la valeur dans le fichier JSON
        global_lock = global_lock_get()
        with global_lock :
            with open(filename, 'w') as f:
                json.dump(value, f)

    def get(self):
        """
        Get the variable
        """




        filename = os.path.join(self.variables_directory, self.name + ".json")
        try:

            """
            DEBUG
            """
            if self.name == "filename_dic":
                a = 3
            
            global_lock = global_lock_get()
            with global_lock :
                with open(filename, 'r') as f:
                    load = json.load(f)
            return load
     
        except Exception as e:
            tb = traceback.format_exc()
            message = f"Erreur lors de la récupération de la variable JSON : {self.name},\ntraceback :\n{tb}"
            print(message)
            return None
        
    def add(self, key, value):
        """
        For dictionnary only
        """
        dict = self.get()
        if dict == None :
            print(f"critical error with variable.add")
        dict[key] = value
        self.set(dict)

def remove_global_variables(global_lock):
    with global_lock :
        shutil.rmtree(variables_directory)
    
    while os.path.exists(variables_directory):
        time.sleep(0.1)  # Attendre 1 seconde
        print("En attente de suppression du répertoire...")
    
    print("Suppression du répertoire terminée.")
    return


def global_variables_init(global_lock):
    """
    Variables init
    """

    Variable("filename_dic").set({})
    Variable("trace_activated").set(False)
    Variable("time_loop_update_account_process").set(60*5)
    Variable("time_loop_update_price_all_process").set(60*5)













































