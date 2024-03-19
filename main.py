"""
Main programm to launch the crypto-notifier process
Author : Thomas Vernoux
Date : March 3, 2024
"""


from process import *
from functions_log import *
from functions_email import *





if __name__ == "__main__":
    try : 
        process()
    except Exception as e:
        tb = traceback.format_exc()
        send_email("Fatal ERROR", f"Crypto-process crash \n{tb}")
        log_error_critic(f"Crypto-process crash \n{tb}")
        