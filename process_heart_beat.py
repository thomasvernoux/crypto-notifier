"""
Date : 2024 04 20
Author : Thomas Vernoux
Subject : 
This Python file contain the Heart Beat Process function. See function details for more informations
"""

from functions_email import *


def ProcessHeartBeat():
    """
    This function get the heartbeat_message variable, 
    and sort the data by datetime. Then, send an email with the informations.
    """
    # Log the function name for traceability
    log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    
    # Define the subject of the email
    subject = "crypto-notifier heart beat"

    # Retrieve the heartbeat message from a variable named "heartbeat_message"
    body_dict = Variable("heartbeat_message").get()

    # Sort the dictionary based on the 'Buy order datetime' value in each item, from newest to oldest
    sorted_crypto = sorted(body_dict.items(), key=lambda x: x[1]['Buy order datetime'], reverse=True)

    # Create the string with the information of each cryptocurrency
    body = ""
    for crypto, info in sorted_crypto:
        # Construct the string for each cryptocurrency with its info
        body += crypto + ": " + "\n".join([f"{k}: {v}" for k, v in info.items()]) + "\n\n"

    # Send the email with the subject and body
    send_email(subject, body)

    return 1




