"""
Basics functions helpfull for the code
Author : Thomas Vernoux
Date : March 3, 2024
"""






#import winsound
import time


from global_variables import *

from functions_log import *

from decimal import Decimal
import inspect
import shutil
import os

from class_cryptos import *

from coinbase.rest import RESTClient



def binary_confirmation(message):
    """
    Print a message and enter yes to continue
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    print(message)
    response = str(input())

    if response == "yes":
        return 
    else : 
        print("negative answer")
        binary_confirmation(message)

def sound_notification():

    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    if Variable("sound_activated").get():
        for i in range(3):
            #winsound.Beep(1000, 2000)
            time.sleep(2)

def truncate_number(number_str, significant_digits=4):

    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    # Convertir la chaîne de caractères en un nombre décimal
    number = Decimal(number_str)
    
    # Tronquer le nombre au nombre de chiffres significatifs spécifié
    number = number.normalize()
    
    digits_after_decimal = 6
    formatted_number = "{:.{}e}".format(number, digits_after_decimal)
    formatted_number = formatted_number.replace("+", "")

    [number1, exponent] = formatted_number.split("e")
    number = number1[:significant_digits+1]

    ret_value = f"{number}e{exponent}"
    return ret_value

def calculate_sell_quantity(product_info, sell_quantity_str):
    """
    This function calculates the quantity that can be sold based on the provided product information and the desired sell quantity.

    Parameters:
        product_info (dict): A dictionary containing information about the product, including base increment, quote increment, and minimum base size.
        sell_quantity_str (str): The desired sell quantity as a string.

    Returns:
        str: The conforming sell quantity that can be sent to the API for sale.

    Description:
        The function first converts the sell quantity to a float and retrieves relevant product information such as base increment, quote increment, and minimum base size.
        It then checks if the requested sell quantity is less than the minimum base size and prints a message if it is.
        Next, it calculates the conforming sell quantity by incrementing by the base increment until it reaches or exceeds the sell quantity.
        The conforming sell quantity is converted back to a string, and if it has more than 3 significant digits, it is truncated using the truncate_number function (implementation not provided).
        Finally, the conforming sell quantity is returned.
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    # Convert to float
    sell_quantity = float(sell_quantity_str)
    
    # copy informations
    base_increment = float(product_info['base_increment'])
    quote_increment = float(product_info['quote_increment'])
    base_min_size = float(product_info['base_min_size'])
    
    
    
    conform_sell_quantuty = 0

    while conform_sell_quantuty + base_increment < sell_quantity:
        conform_sell_quantuty += base_increment
    
    # check is the amount is enough
    if conform_sell_quantuty < base_min_size : 
        print("cannot sell : quantity too low")
        log_error_minor("cannot sell : quantity too low")

    conform_sell_quantuty = str(conform_sell_quantuty)
    if len(conform_sell_quantuty) > 3:
        conform_sell_quantuty = truncate_number(conform_sell_quantuty, significant_digits=3)

    
    return conform_sell_quantuty    

def delete_directory_if_exists(directory_path):
    """
    Check if the directory exists and delete it if it exists.

    Args:
    directory_path (str): The path to the directory to be deleted.

    Returns:
    None
    """

    # Check if the directory exists
    if os.path.exists(directory_path):
        try:
            # Delete the directory and its contents
            shutil.rmtree(directory_path)
            #print("Directory deleted successfully.")
        except OSError as e:
            print(f"Error: {directory_path} : {e.strerror}")
            
    else:
        #print("Directory does not exist.")
        None


