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

def get_last_buy_price(orders,crypto):
    """
    Return last buy price for a crypto
    inputs : 
    orders : list of all orders
    crypto : crypto class object
    """

    log_trace(str(inspect.currentframe().f_back.f_code.co_name) + f" {crypto.name}")
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

def test_truncate_number():
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    input_values = ["1", "2.123456789876", "0.999991567", "0.00000000005679988"]
    expected_output = ["1.000e0", "2.123e0", "9.999e-1", "5.679e-11"]
    significant_digits = 4

    output = [truncate_number(str(value), significant_digits) for value in input_values]
    
    if expected_output == output:
        return True
    else : 
        log_error_critic("error in test truncate number")

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

def tests_calculate_sell_quantity():
    """
    Function to test the calculation of sell quantity for a given product.

    Args:
        None

    Returns:
        bool: True if the test passes, False otherwise.

    Description:
    This function tests the calculation of sell quantity for a given product.
    It calculates the sell quantity based on the provided product information and input value.
    Then, it compares the calculated sell quantity with the expected output.
    If the calculated sell quantity matches the expected output, it returns True,
    otherwise, it logs an error and returns False.
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    # Sample product information
    product = {
        'product_id': 'SEAM-USDC',
        'price': '4.2229',
        'price_percentage_change_24h': '-7.31530661516176',
        'volume_24h': '49758.5',
        'volume_percentage_change_24h': '-36.36540352788765',
        'base_increment': '0.1',
        'quote_increment': '0.0001',
        'quote_min_size': '2',
        'quote_max_size': '10000000',
        'base_min_size': '0.1',
        'base_max_size': '30303030.303030303030303',
        'base_name': 'Seamless',
        'quote_name': 'USDC',
        'watched': False,
        'is_disabled': False,
        'new': False,
        'status': 'online',
        'cancel_only': False,
        'limit_only': False,
        'post_only': False,
        'trading_disabled': False,
        'auction_mode': False,
        'product_type': 'SPOT',
        'quote_currency_id': 'USDC',
        'base_currency_id': 'SEAM',
        'fcm_trading_session_details': None,
        'mid_market_price': '',
        'alias': 'SEAM-USD',
        'alias_to': [],
        'base_display_symbol': 'SEAM',
        'quote_display_symbol': 'USD',
        'view_only': False,
        'price_increment': '0.0001',
        'display_name': 'SEAM-USDC',
        'product_venue': 'CBE'
    }

    # Input values for the test
    input_values = ["0.800123798"]
    
    # Expected output for the test
    expected_output = ["8.00e-1"]

    # Calculating sell quantity based on the product and input values
    output = [calculate_sell_quantity(product, value) for value in input_values]

    # Comparing calculated sell quantity with expected output
    if expected_output == output:
        return True
    else:
        # Logging an error if the test fails
        log_error_critic("tests_calculate_sell_quantity")

    return False 





#test_truncate_number()
#tests_calculate_sell_quantity()
