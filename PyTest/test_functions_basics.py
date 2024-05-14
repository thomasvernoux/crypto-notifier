"""
Date : 2024/05/13
Author : Thomas Vernoux

"""




import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Add the absolute path of the parent directory to sys.path
sys.path.append(parent_dir)




from global_variables import *

from functions_basics import * 

Variable("sell_activated").set(False)  # test or real
Variable("coinbase_api_call_activated").set(False)  # test or real



def test_truncate_number():

    assert truncate_number(number_str = "12", significant_digits=2) == "1.2e1"
    assert truncate_number(number_str = "1", significant_digits=4) == "1.000e0"

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

    

   

    assert calculate_sell_quantity(product, "0.800123798") == "8.00e-1"


