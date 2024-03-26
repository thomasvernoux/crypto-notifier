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

table_name = "ADA"
last_index = get_last_index(table_name)


plot_from_json("strategy tester/ada_price_history.csv")






















