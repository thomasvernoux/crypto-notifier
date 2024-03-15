


import functions_SQLite
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

import inspect

from functions_log import *

def plot_crypto(crypto_name=None):

    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    # Retrieve data
    x, y = functions_SQLite.get_crypto_price_history_pyplotable(crypto_name, db_file="SQL_database/crypto.db")

    # Convert timestamps to numerical values
    x_numeric = [float(timestamp) for timestamp in x]

    # Convert numerical timestamps to datetime objects
    x_datetime = [datetime.fromtimestamp(timestamp) for timestamp in x_numeric]

    # Plot the data
    plt.plot(x_datetime, y)

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title(f'Price History of {crypto_name}')

    # Format x-axis ticks as dates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Show the plot
    plt.tight_layout()
    plt.show()













