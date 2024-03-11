"""
Main programm to launch the crypto-notifier process
"""


from process import *
from functions_log import *
from functions_email import *




if __name__ == "__main__":
    try : 
        process()
    except Exception as e:
        send_email("Fatal ERROR", f"Crypto-process crash \n{e}")
        log_error_critic(f"Crypto-process crash \n{e}")
        