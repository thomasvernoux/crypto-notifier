


from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *
from global_variables import *
from class_crypos import *

set_variable_mode("test")

all_test_passed = True

def test_peak_detection1():
    """ 
    Simple peak detection test
    """

    global all_test_passed
    set_variable_test_mail_send(False)

    crypto1 = Crypto()
    crypto1.name = "Test01"
    crypto1.amount = 8                 
    crypto1.buy_price = 30               
    crypto1.max_price = 120                 
    crypto1.current_price = 105            
    crypto1.USDC_balance = 1             
    crypto1.number_of_alert_authorized = 1  
    crypto1.last_notification_time = 0       
    crypto1.peak_target = 95   
    crypto1.break_even_point = 105              


    crypto1.cryptoprocess()



    if not( get_variable_test_mail_send()):
        all_test_passed = False
        print("test_peak_detection1 failed")

def test_peak_detection2():
    """ 
    Simple peak detection test
    Out of notification authorized
    """

    global all_test_passed
    set_variable_test_mail_send(False)

    crypto1 = Crypto()
    crypto1.name = "Test01"
    crypto1.amount = 8                 
    crypto1.buy_price = 30               
    crypto1.max_price = 120                 
    crypto1.current_price = 105            
    crypto1.USDC_balance = 1             
    crypto1.number_of_alert_authorized = 0  
    crypto1.last_notification_time = 0       
    crypto1.peak_target = 95   
    crypto1.break_even_point = 105              


    crypto1.cryptoprocess()



    if get_variable_test_mail_send():
        all_test_passed = False
        print("test_peak_detection 2 failed")

def test_peak_detection3():
    """ 
    current price too low, under buy price * break_even_point
    """

    global all_test_passed
    set_variable_test_mail_send(False)

    crypto1 = Crypto()
    crypto1.name = "Test01"
    crypto1.amount = 8                 
    crypto1.buy_price = 119               
    crypto1.max_price = 120                 
    crypto1.current_price = 105            
    crypto1.USDC_balance = 1             
    crypto1.number_of_alert_authorized = 1  
    crypto1.last_notification_time = 0       
    crypto1.peak_target = 95   
    crypto1.break_even_point = 105              


    crypto1.cryptoprocess()



    if get_variable_test_mail_send():
        all_test_passed = False
        print("test_peak_detection 3 failed")

def test_peak_detection4():
    """ 
    Price still growing
    """

    global all_test_passed
    set_variable_test_mail_send(False)

    crypto1 = Crypto()
    crypto1.name = "Test01"
    crypto1.amount = 8                 
    crypto1.buy_price = 30               
    crypto1.max_price = 120                 
    crypto1.current_price = 121            
    crypto1.USDC_balance = 1             
    crypto1.number_of_alert_authorized = 1  
    crypto1.last_notification_time = 0       
    crypto1.peak_target = 95   
    crypto1.break_even_point = 105              


    crypto1.cryptoprocess()


    if get_variable_test_mail_send():
        all_test_passed = False
        print("test_peak_detection 4 failed")

def test_peak_detection5():
    """ 
    Price not under the peak target
    """

    global all_test_passed
    set_variable_test_mail_send(False)

    crypto1 = Crypto()
    crypto1.name = "Test01"
    crypto1.amount = 8                 
    crypto1.buy_price = 30               
    crypto1.max_price = 120                 
    crypto1.current_price = crypto1.max_price * 95.1/100            
    crypto1.USDC_balance = 1             
    crypto1.number_of_alert_authorized = 1  
    crypto1.last_notification_time = 0       
    crypto1.peak_target = 95   
    crypto1.break_even_point = 105              


    crypto1.cryptoprocess()



    if get_variable_test_mail_send():
        all_test_passed = False
        print("test_peak_detection 5 failed")




test_peak_detection1()    # Simple peak detection test
test_peak_detection2()    # out of notification test
test_peak_detection3()    # current price under buy price test
test_peak_detection4()    # price still growing
test_peak_detection5()    # price not under peak target


print("All tests passed : ", all_test_passed)
