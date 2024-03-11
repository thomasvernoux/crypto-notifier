"""
Log module V1.0
A simple module to manage errors
Author : Thomas Vernoux
Date : 06/03/2023
"""


import traceback
import os

from datetime import datetime
from functions_basics import *


# Variable to store the path of the error log file
log_base_path = "log"

filename_dic = {}

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

def init_error_module(file):
    """
    Initializes a new error log file with the current date and time.
    """
    global error_file_path
    global filename_dic

    keep_recent_files(f"{log_base_path}/{file}")

    # Generate a timestamp for the error log file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create the file path for the error log file
    file_path = f"{log_base_path}/{file}/{timestamp}.txt"
    filename_dic[file] = file_path

    check_and_create_directory(log_base_path)
    check_and_create_directory(f"{log_base_path}/{file}")
    # Create the error log file and write an initial header
    with open(file_path, "w") as error_file:
        error_file.write(f"=== Errors ({timestamp}) ===\n")
    return

def write_log(file, error_message):
    """
    Adds an error message to the error log file.
    """
    
    global filename_dic

    try : 
        error_message = str(error_message)
    except Exception as e:
        print("Error while converting error message in str")
        tb = traceback.format_exc()
        print(tb)

    
    if not (file in filename_dic) : 
        init_error_module(file)

    # Open the error log file in append mode and write the error message
    with open(filename_dic[file], "a") as error_file:
        error_file.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " : " + error_message + "\n")
    
    """
    Write everithing in a full log file
    """
    full_log_name = "full_log"
    full_log_path = log_base_path + "/" + full_log_name
    
    if not (full_log_name in filename_dic) : 
        init_error_module(full_log_name)

    with open(filename_dic["full_log"], "a") as error_file:
        error_file.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " : " + error_message + "\n")

def critical_error(error_message):
    """
    Logs a critical error message and terminates the program.

    Parameters:
    - error_message (str): The error message to be logged.

    This function logs the given error message as a critical error in the error log file,
    prints a notification about the critical error, and terminates the program.
    """
    # Log the critical error message
    write_log("errors", "CRITICAL error: " + error_message)

    # Print a notification about the critical error
    print("Critical error detected. Please check the error log file for more details.")

    # Terminate the program
    exit()

def minor_error(error_message):
    """
    Logs a minor error message.

    Parameters:
    - error_message (str): The error message to be logged.

    This function logs the given error message as a minor error in the error log file
    and prints a notification about the minor error.
    """
    # Log the minor error message
    write_log("errors", "Minor error: " + error_message)

    # Print a notification about the minor error
    print("Minor error detected. Please check the error log file for more details.")

    # Return control back to the caller
    return



"""
Usage example

minor_error("test 02")
write_log("test", "hello")
critical_error("test 01")


"""



