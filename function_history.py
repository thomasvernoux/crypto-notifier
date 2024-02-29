
import time

def save_to_file(crypto):
    """
    Sauvegarde le cours de la crypto dans un fichier texte.
    """
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