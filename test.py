


from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *
from cryptoprocess import *
from global_variables import *

set_variable_mode("test")

all_test_passed = True

def test_peak_detection1():
    """ 
    Should detect a peak
    """

    set_variable_test_mail_send(False)

    crypto1 = Crypto()
    crypto1.name = "Test01"
    crypto1.amount = 8                 
    crypto1.buy_price = 1               
    crypto1.max_price = 10                 
    crypto1.current_price = 8             
    crypto1.USDC_balance = 1             
    crypto1.number_of_alert_authorized = 1  
    crypto1.last_notification_time = 0       
    crypto1.peak_target = 80                  


    crypto_process(crypto1)



    if not( get_variable_test_mail_send()):
        all_test_passed = False
        print("test_peak_detection1")

def test_peak_detection2():
    """ 
    Should not detect a peak
    """

    set_variable_test_mail_send(False)

    crypto1 = Crypto()
    crypto1.name = "Test02"
    crypto1.amount = 1                 
    crypto1.buy_price = 0.10               
    crypto1.max_price = 1                 
    crypto1.current_price = 0.81             
    crypto1.USDC_balance = 1             
    crypto1.number_of_alert_authorized = 1  
    crypto1.last_notification_time = 0       
    crypto1.peak_target = 80                  


    crypto_process(crypto1)

    

    if get_variable_test_mail_send():
        all_test_passed = False
        print("test_peak_detection 2")

test_peak_detection1()
test_peak_detection2()

print("All tests passed : ", all_test_passed)
