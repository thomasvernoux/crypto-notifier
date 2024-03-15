"""
Author : Thomas Vernoux
Date : March 12, 2024

Filename: crypto_database_operations.py

Description:
This file contains functions for managing an SQLite database used for storing cryptocurrency data. It includes functions for checking the existence of the database, adding values to the database, and retrieving and optionally printing the contents of the database table.

Functions:
1. check_database_exist(db_file="SQL_database/crypto.db"):
   - Description: Checks if the SQLite database exists and creates it if it doesn't. It also creates the directory containing the database if necessary.
   - Parameters:
     - db_file (str): Path of the SQLite database file. Default is "SQL_database/crypto.db".

2. add_value(crypto_name, data_tuple, db_file="SQL_database/crypto.db"):
   - Description: Adds a value to the specified SQL database table. It checks if the database exists, creating it if necessary. Then, it establishes a connection to the database, creates the table if it doesn't exist yet, inserts the provided data into the table, commits the transaction, and closes the connection.
   - Parameters:
     - crypto_name (str): Name of the table where the value will be added.
     - data_tuple (tuple): A tuple containing the time and value to be inserted into the table.
     - db_file (str): Path of the SQLite database file. Default is "SQL_database/crypto.db".

3. get_print_database_table(crypto_name, db_file="SQL_database/crypto.db", Print=True):
   - Description: Retrieves and optionally prints the contents of the specified SQL database table. It checks if the database exists, creating it if necessary. Then, it establishes a connection to the database, retrieves the data from the table, optionally prints the retrieved data, and returns it as a list of tuples.
   - Parameters:
     - crypto_name (str): Name of the table to retrieve data from.
     - db_file (str): Path of the SQLite database file. Default is "SQL_database/crypto.db".
     - Print (bool): Whether to print the retrieved data. Default is True.
"""

import sqlite3
import os
import functions_log
import functions_log
import inspect
from functions_log import *


def check_database_exist(db_file="SQL_database/crypto.db"):
    """
    Check if the SQLite database exists, create it if it doesn't.
    
    Parameters:
    - db_file (str): Path of the SQLite database file. By default, it's set to "SQL_database/crypto.db".
    
    Description:
    This function checks if the SQLite database exists. If it doesn't exist, it also creates the directory containing the database if necessary.
    If the database file doesn't exist, the function creates it. If the directory specified in the database file path doesn't exist, the function also creates the directory.

    Returns:
    No return value.
    """

    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    # Extract the directory from the database file path
    db_dir = os.path.dirname(db_file)

    # Check if the directory exists, create it if it doesn't
    if not os.path.exists(db_dir):
        print(f"The directory '{db_dir}' does not exist. Creating it...")
        os.makedirs(db_dir)
        print(f"The directory '{db_dir}' has been created.")

    # Check if the database file exists
    if not os.path.exists(db_file):
        # If the database file doesn't exist, create it
        functions_log.log_write(error_message = f"The database '{db_file}' does not exist. Creating it...")
        conn = sqlite3.connect(db_file)
        conn.close()
        functions_log.log_write(error_message = f"The database '{db_file}' has been created.")
    else:
        functions_log.log_write(error_message = f"The database '{db_file}' already exists.")

def add_value(crypto_name, data_tuple, db_file="SQL_database/crypto.db"):
    """
    Add a value to an SQL database table.

    Parameters:
    - crypto_name (str): Name of the table where the value will be added.
    - data_tuple (tuple): A tuple containing the time and value to be inserted into the table.
    - db_file (str): Path of the SQLite database file. Default is "SQL_database/crypto.db".

    Description:
    This function adds a value to the specified SQL database table. It first checks if the database exists, creating it if necessary.
    Then, it establishes a connection to the database, creates the table if it doesn't exist yet, inserts the provided data into the table,
    commits the transaction, and finally closes the connection.

    Returns:
    None
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    # Check if the database exists, create it if necessary
    check_database_exist(db_file)

    # Unpack the tuple
    time, value = data_tuple

    # Establish connection to the database
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    # Create the table if it doesn't exist
    cur.execute(f"CREATE TABLE IF NOT EXISTS {crypto_name} (time TEXT, value_USDC REAL)")

    # Insert the data into the table
    cur.execute(f"INSERT INTO {crypto_name} VALUES (?, ?)", (time, value))

    # Commit the transaction and close the connection
    con.commit()
    con.close()

    return

def get_print_database_table(crypto_name, db_file="SQL_database/crypto.db", Print=True):
    """
    Retrieve and optionally print the contents of an SQL database table.

    Parameters:
    - crypto_name (str): Name of the table to retrieve data from.
    - db_file (str): Path of the SQLite database file. Default is "SQL_database/crypto.db".
    - Print (bool): Whether to print the retrieved data. Default is True.

    Description:
    This function retrieves the contents of the specified SQL database table. It first checks if the database exists,
    creating it if necessary. Then, it establishes a connection to the database, retrieves the data from the table,
    optionally prints the retrieved data, and returns it as a list of tuples.

    Returns:
    list: A list containing the retrieved data.
    """
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    # Check if the database exists, create it if necessary
    check_database_exist(db_file)

    ret_value = []

    # Establish connection to the database
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    # Retrieve data from the table
    for row in cur.execute(f"SELECT time, value_USDC FROM {crypto_name}"):
        if Print:
            print(row)
        ret_value.append(row)

    # Close the connection
    con.close()

    return ret_value

def get_crypto_price_history_pyplotable(crypto_name, db_file="SQL_database/crypto.db"):
    
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    check_database_exist(db_file)

    ret_value = [[], []]

    # Establish connection to the database
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    # Retrieve data from the table
    for row in cur.execute(f"SELECT time, value_USDC FROM {crypto_name}"):
        
        ret_value[0].append(row[0])
        ret_value[1].append(row[1])

    # Close the connection
    con.close()

    return ret_value


