"""
Basics functions helpfull for the code
Author : Thomas Vernoux
Date : March 3, 2024
"""






import winsound
import time


from global_variables import *

from functions_log import *

from decimal import Decimal






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

    if get_variable_sound_activated():
        for i in range(3):
            winsound.Beep(1000, 2000)
            time.sleep(2)

def get_last_buy_price(orders,crypto):
    """
    Return last buy price for a crypto
    inputs : 
    orders : list of all orders
    crypto : crypto class object
    """


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

def truncate_number(number_str, significant_digits=4):


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

def test_truncate_number():
    input_values = ["1", "2.123456789876", "0.999991567", "0.00000000005679988"]
    expected_output = ["1.000e0", "2.123e0", "0.999e-1", "5.679e-11"]
    significant_digits = 4

    output = [truncate_number(str(value), significant_digits) for value in input_values]
    
    if expected_output == output:
        return True
        


test_truncate_number()
