"""
Python script for updating cryptocurrency prices and related operations.
Author: Thomas Vernoux
Date: March 22, 2024

This script contains functions to update cryptocurrency prices, manage balances in USDC, calculate maximum prices, and store data in a SQLite database.

Functions:
1. ProcessUpdatePrice_ALL(): Updates prices for all cryptocurrencies.
2. ProcessUpdatePrice(): Updates prices for cryptocurrencies with USDC balance > 0.5.
"""

import time
from functions_crypto import *
from functions_email import *
from functions_specials_alerts import *
from functions_log import *
from class_cryptos import *
from functions_basics import *
import inspect

import functions_SQLite





def update_crypto_prices(cryptos_list, min_usdc_balance=None):
    """
    Update prices of cryptocurrencies in cryptos_list.
    If min_usdc_balance is specified, only update prices for cryptocurrencies with USDC balance > min_usdc_balance.
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    for crypto in cryptos_list:
        if min_usdc_balance is None or crypto.USDC_balance > min_usdc_balance:
            # Update information for an individual cryptocurrency
            update_single_crypto(crypto)

def update_single_crypto(crypto):
    """
    Update price, USDC balance, max price, and store data in SQLite database for a single cryptocurrency.
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name) + crypto.name)
    try:
        # Get the current price of the cryptocurrency
        crypto.current_price = get_price(crypto)
        # Update the USDC balance for the cryptocurrency
        crypto.update_USDC_balance()
        # Update the maximum recorded price for the cryptocurrency
        crypto.update_max_price()
        # Store the current price in the SQLite database
        functions_SQLite.add_value(crypto_name=crypto.name, data_tuple=(time.time(), crypto.current_price))


    except KeyboardInterrupt:
        # Catch a keyboard interruption (Ctrl+C) and display a message
        print(f"End of update for {crypto.name}")

def ProcessUpdatePrice_ALL():
    """
    Update prices for all cryptocurrencies.
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    try:
        # Display a message indicating the start of the process
        print("Updating prices for all cryptocurrencies")
        # Write the start of the process to the logs
        log_write("working process", "ProcessUpdatePrice_ALL")
        # Initialize an object containing the cryptocurrencies
        CRYPTOS_object = CRYPTOS()
        # Get data about the cryptocurrencies
        CRYPTOS_object.getCRYPTO_json()
        # Update prices for all cryptocurrencies
        update_crypto_prices(CRYPTOS_object.cryptos_list)
        # Write the updated data to the JSON file
        CRYPTOS_object.writeCRYPTO_json()
    except KeyboardInterrupt:
        # Catch a keyboard interruption (Ctrl+C) and display a message
        print("Keyboard interruption detected. End of ProcessUpdatePrice_ALL")

def ProcessUpdatePrice():
    """
    Update prices for cryptocurrencies with USDC balance > 0.5.
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    # Write the start of the process to the logs
    log_write("working process", "ProcessUpdatePrice")
    try:
        # Initialize an object containing the cryptocurrencies
        CRYPTOS_object = CRYPTOS()
        # Get data about the cryptocurrencies
        CRYPTOS_object.getCRYPTO_json()
        # Update prices for cryptocurrencies with USDC balance > 0.5
        update_crypto_prices(CRYPTOS_object.cryptos_list, min_usdc_balance=0.5)
        # Write the updated data to the JSON file
        CRYPTOS_object.writeCRYPTO_json()
    except KeyboardInterrupt:
        # Catch a keyboard interruption (Ctrl+C) and display a message
        print("End of ProcessUpdatePrice")

