

from coinbase.wallet.client import Client
import json


def load_var_from_json(filename, variable):
    """
    Load a variable from json
    @filename : path to json
    @variable : name of the variable to find in the json
    """
    with open(filename, 'r') as file:
        keys = json.load(file)
    return keys[variable]


api_key  = load_var_from_json('api_keys/api_key_001.json', "api_key")
api_secret = load_var_from_json('api_keys/api_key_001.json', "api_secret")



client = Client(api_key, api_secret)
user = client.get_current_user()
#print(user)
p = client.get_buy_price(currency_pair = 'BTC-USD')
#print(p)


accounts = client.get_accounts()
print(accounts)