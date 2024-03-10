







import winsound
import time







def binary_confirmation(message):
    """
    Print a message and enter yes to continue
    """

    print(message)
    response = str(input())

    if response == "yes":
        return 
    else : 
        print("negative answer")
        binary_confirmation(message)



def sound_notification():


    for i in range(10):
        # winsound.Beep(1000, 2000)
        time.sleep(2)

def get_last_buy_price(orders,crypto):
    """
    Return last buy price for a crypto
    inputs : 
    orders : list of all orders
    crypto : crypto class object
    """


    """
    Debug
    """
    if crypto.name == "VARA":
        a = 3

    orders = orders["orders"]
    fitting_orders = []
    for i in orders : 
        ### Select right orders
        if not(i["product_id"] == f"{crypto.coinbaseId}-USDC"):
            continue
        if i["completion_percentage"] == 0:
            continue
        if i["side"] == "SELL" :
            continue
        if i["status"] != "FILLED" :
            continue
        
        fitting_orders.append(i)
    
    if fitting_orders == []:
        return []
    
    elif len(fitting_orders) == 1:
        return float(fitting_orders[0]["average_filled_price"])

    elif len(fitting_orders) > 1:
        # find the last order
        the_last_oder = fitting_orders[0]
        for i in fitting_orders[1:]:
            if i["created_time"] > the_last_oder["created_time"]:
                the_last_oder = i
        price = float(the_last_oder["average_filled_price"])
        return price



