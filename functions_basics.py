







import winsound
import time

import os
import glob
import heapq
from datetime import datetime






def binary_confirmation(message):
    """
    Print a message and enter yes to continue
    """

    print(message)
    response = str(input())

    if response == "yes":
        return 
    else : 
        print("negative answer")
        binary_confirmation(message)



def sound_notification():


    for i in range(10):
        winsound.Beep(1000, 2000)
        time.sleep(2)

def get_last_buy_price(orders,crypto):
    """
    Return last buy price for a crypto
    inputs : 
    orders : list of all orders
    crypto : crypto class object
    """


    """
    Debug
    """
    if crypto.name == "VARA":
        a = 3

    orders = orders["orders"]
    fitting_orders = []
    for i in orders : 
        ### Select right orders
        if not(i["product_id"] == f"{crypto.coinbaseId}-USDC"):
            continue
        if i["completion_percentage"] == 0:
            continue
        if i["side"] == "SELL" :
            continue
        if i["status"] != "FILLED" :
            continue
        
        fitting_orders.append(i)
    
    if fitting_orders == []:
        return []
    
    elif len(fitting_orders) == 1:
        return float(fitting_orders[0]["average_filled_price"])

    elif len(fitting_orders) > 1:
        # find the last order
        the_last_oder = fitting_orders[0]
        for i in fitting_orders[1:]:
            if i["created_time"] > the_last_oder["created_time"]:
                the_last_oder = i
        price = float(the_last_oder["average_filled_price"])
        return price


def keep_recent_files(path):
    """
    This function takes a path as input and deletes all files except the three most recent ones in the given directory.

    Parameters:
    - path: The path to the directory where files need to be processed and deleted.

    Behavior:
    - If the specified path is not a directory, a message indicating the same is printed, and the function returns.
    - If there are three or fewer files in the directory, a message indicating that no files will be deleted is printed, and the function returns.
    - Otherwise, the function retrieves the list of files in the directory along with their modification timestamps.
    - It then selects the three most recent files based on their timestamps.
    - All files in the directory that are not among the three most recent ones are deleted.
    - During the deletion process, a message indicating the deletion of each file is printed.

    Note: This function permanently deletes files from the directory, so use it with caution.

    """
    # Vérifier si le chemin d'accès est un répertoire
    if not os.path.isdir(path):
        print("Le chemin spécifié n'est pas un répertoire.")
        return
    
    # Obtenir la liste de tous les fichiers dans le répertoire
    files = glob.glob(os.path.join(path, "*"))
    
    # Si le nombre de fichiers est inférieur ou égal à 3, aucun fichier ne doit être supprimé
    if len(files) <= 3:
        print("Il y a 3 fichiers ou moins dans le répertoire. Aucun fichier ne sera supprimé.")
        return
    
    # Créer une liste des fichiers avec leur date de modification
    files_with_timestamp = [(file, os.path.getmtime(file)) for file in files]
    
    # Obtenir les trois fichiers les plus récents
    recent_files = heapq.nlargest(3, files_with_timestamp, key=lambda x: x[1])
    
    # Supprimer tous les fichiers qui ne sont pas dans les trois plus récents
    for file, _ in files_with_timestamp:
        if (file, _) not in recent_files:
            os.remove(file)
            print(f"Suppression du fichier {file}")


