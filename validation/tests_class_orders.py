import sys
sys.path.append('./')

from old.class_order import *
from coinbase.rest import RESTClient

client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
orders = client.list_orders()['orders']


for order in orders :
    o = OrderHistory(order)
    print(o.get_str_printable())






