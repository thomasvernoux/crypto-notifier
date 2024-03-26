"""
Date : 2024 - 03 - 26
Author : Thomas Vernoux
"""


import sys
sys.path.append('./')
from functions_plot import *
from class_cryptos import *
import sqlite3
from functions_plot import *
import json


from strategy_tester_functions import *


tables_counts = list_tables_and_counts(db_file="SQL_database/crypto.db")

for table, count in tables_counts.items():
        if count > 5000:
            print(f"Table '{table}' contains {count} rows.")
            plot_crypto(table)
            

























