
import time

def save_to_file(crypto):
    """
    Sauvegarde le cours de la crypto dans un fichier texte.
    """
    filename = f"{crypto.name}_cours.txt"
    file = open(f"cours/{filename}", 'a')    
    file.write(f"{int(time.time())}, {crypto.current_price}\n")
    file.close()