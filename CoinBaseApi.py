

from coinbase.wallet.client import Client
import json
from global_variables import *


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

def get_accounts_from_api():

    client = Client(api_key, api_secret)
    user = client.get_current_user()
    #print(user)
    p = client.get_buy_price(currency_pair = 'BTC-USD')
    #print(p)


    accounts = client.get_accounts()
    return accounts

def get_sell_price(crypto):
    
    # TODO

    # client.get_sell_price(currency_pair = 'BTC-USD')

    return None


def update_account_id_dico():
    client = Client(api_key, api_secret)
    accounts = client.get_accounts()
    
    global dico_account_id
    dico_account_id = {}
    for i in accounts["data"]:
        key = i.currency.code
        value = i.currency.asset_id
        dico_account_id[key] = value

    set_variable_dico_account_id(dico_account_id)

