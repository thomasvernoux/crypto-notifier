"""
2024 03 26 ada crypto is not in accounts, have to be debbuged
resolved : 
client.get_accounts was limited to 49 accounts
solution : 
client.get_accounts(250)
"""



import sys
sys.path.append('./')

from class_cryptos import *
from functions_basics import *



client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
accounts = client.get_accounts(250)["accounts"]
print(len(accounts))

for a in accounts : 
    print(a["currency"], a["available_balance"]["value"])
