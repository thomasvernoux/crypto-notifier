
"""
Functions linked to the crypto history feature
Author : Thomas Vernoux
Date : March 3, 2024
"""


import time
import os

def check_and_create_directory(directory_path):
    """
    Vérifie si le répertoire existe, et le crée s'il n'existe pas.

    Parameters:
    - directory_path (str): Le chemin du répertoire à vérifier et créer.

    Returns:
    - bool: True si le répertoire existe ou a été créé avec succès, False sinon.
    """
    # Vérifie si le répertoire existe
    if not os.path.exists(directory_path):
        try:
            # Crée le répertoire s'il n'existe pas
            os.makedirs(directory_path)
            #print(f"Le répertoire '{directory_path}' a été créé avec succès.")
            return True
        except OSError as e:
            #print(f"Erreur lors de la création du répertoire '{directory_path}': {e}")
            return False
    else:
        #print(f"Le répertoire '{directory_path}' existe déjà.")
        return True
    

def save_to_file(crypto):
    """
    Sauvegarde le cours de la crypto dans un fichier texte.
    """
    check_and_create_directory("cours")
    filename = f"{crypto.name}_cours.txt"
    file = open(f"cours/{filename}", 'a')    
    file.write(f"{int(time.time())}, {crypto.current_price}\n")
    file.close()


def read_last_values_fichier(crypto, x):
    valeurs = []
    filename = f"{crypto.name}_cours.txt"
    with open(f"cours/{filename}", 'r') as file:
        # Lire les x dernières lignes du fichier
        lines = file.readlines()[-x:]
        for line in lines:
            # Séparer les valeurs en utilisant la virgule comme séparateur
            timestamp, value = line.strip().split(', ')
            # Ajouter les valeurs à la liste
            valeurs.append((int(timestamp), float(value)))
    return valeurs