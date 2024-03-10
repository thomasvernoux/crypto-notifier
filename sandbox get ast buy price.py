



from coinbase.rest import RESTClient
from class_crypos import *




product = "DOGE"
product_id = "DOGE-USDC"
client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
orders = client.list_orders()

crypto = Crypto()
crypto.coinbaseId = "AUCTION"



def get_lat_buy_price(orders,crypto):
    """
    Return last buy price for a crypto
    inputs : 
    orders : list of all orders
    crypto : crypto class object
    """

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
        return fitting_orders[0]["average_filled_price"]

    elif len(fitting_orders) > 1:
        # find the last order
        the_last_oder = fitting_orders[0]
        for i in fitting_orders[1:]:
            if i["created_time"] > the_last_oder["created_time"]:
                the_last_oder = i
        price = float(the_last_oder["average_filled_price"])
        return price
    

price = get_lat_buy_price(orders,crypto)
print(orders)



