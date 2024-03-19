
"""
This file contain global variables getters and setters
Author : Thomas Vernoux
Date : March 3, 2024
"""

import json
import os

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
        with open(filename, 'w') as f:
            json.dump(value, f)

    def get(self):
        """
        Get the variable
        """
        filename = os.path.join(self.variables_directory, self.name + ".json")
        try:
            # Charger la valeur à partir du fichier JSON
            with open(filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print(f"Erreur lors de la récupération de la variable JSON : {self.name}")
            return None
        
    def add(self, key, value):
        """
        For dictionnary only
        """
        dict = self.get()
        dict[key] = value
        self.set(dict)

"""
Variables init
"""

Variable("trace_activated").set(False)
Variable("time_loop_update_account_process").set(60*5)
Variable("time_loop_update_price_all_process").set(60*5)














































