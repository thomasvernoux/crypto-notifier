"""
Log module V1.0
A simple module to manage errors
Author : Thomas Vernoux
Date : March 6, 2024
"""


import traceback
import os

from datetime import datetime

import glob
import heapq
from global_variables import *

from global_variables import *


# Variable to store the path of the error log file
log_base_path = "log"

variable_name_filename_dic = "filename_dic"    # name of the variable for filename_dic

# init filename_dic. It is the global variable dict that contain file name for log files
Variable(variable_name_filename_dic).set({})


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

def init_error_module(file, persistant = False):
    """
    Initializes a new error log file with the current date and time.
    persistant = True to keep data foreever
    """
    global error_file_path

    if not(persistant):
        keep_recent_files(f"{log_base_path}/{file}")

    # Generate a timestamp for the error log file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create the file path for the error log file
    file_path = f"{log_base_path}/{file}/{timestamp}.txt"
    Variable("filename_dic").add(file, file_path)
    


    check_and_create_directory(log_base_path)
    check_and_create_directory(f"{log_base_path}/{file}")
    # Create the error log file and write an initial header
    with open(file_path, "w") as error_file:
        error_file.write(f"=== Errors ({timestamp}) ===\n")
    return

def log_write(file = "full_log", error_message = None, persistant = False):
    """
    Adds an error message to the error log file.
    """
    

    try : 
        error_message = str(error_message)
    except Exception as e:
        print("Error while converting error message in str")
        tb = traceback.format_exc()
        print(tb)

    
    if not (file in Variable(variable_name_filename_dic).get()) : 
        init_error_module(file, persistant = persistant)

    # Open the error log file in append mode and write the error message
    with open(Variable(variable_name_filename_dic).get()[file], "a") as error_file:
        error_file.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " : " + error_message + "\n")
    
    """
    Write everithing in a full log file
    """
    full_log_name = "full_log"
    full_log_path = log_base_path + "/" + full_log_name
    
    if not (full_log_name in Variable(variable_name_filename_dic).get()) : 
        init_error_module(full_log_name)

    with open(Variable(variable_name_filename_dic).get()["full_log"], "a") as error_file:
        error_file.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " : " + error_message + "\n")

def log_error_critic(error_message : str):
    """
    Logs a critical error message and terminates the program.

    Parameters:
    - error_message (str): The error message to be logged.

    This function logs the given error message as a critical error in the error log file,
    prints a notification about the critical error, and terminates the program.
    """

    # Log the critical error message
    log_write("errors", "CRITICAL error: " + error_message)

    # Print a notification about the critical error
    print("Critical error detected. Please check the error log file for more details.")




def log_error_minor(error_message):
    """
    Logs a minor error message.

    Parameters:
    - error_message (str): The error message to be logged.

    This function logs the given error message as a minor error in the error log file
    and prints a notification about the minor error.
    """
    # Log the minor error message
    log_write("errors", "Minor error: " + error_message)

    # Print a notification about the minor error
    print("Minor error detected. Please check the error log file for more details.")

    # Return control back to the caller
    return

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

    return 

def log_trace(message):
    file = "trace txt"
    """
    DEBUG
    """
    debug = Variable("trace_activated").get()
    if Variable("trace_activated").get() == False :
        return
    
    dict_variable_name_filename_dic = Variable(variable_name_filename_dic).get()
    if dict_variable_name_filename_dic == None :
        init_error_module(file, persistant = False)
    if not (file in dict_variable_name_filename_dic) : 
        init_error_module(file, persistant = False)
    
    with open(Variable(variable_name_filename_dic).get()[file], "a") as error_file:
        error_file.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " : " + message + "\n")

    return




"""
Usage example

log_error_minor("test 02")
log_write("test", "hello")
log_error_critic("test 01")


"""



