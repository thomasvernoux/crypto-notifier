"""
This file contain The 2 classes :
Crypto - Class to manage a crypto
CRYOTOS - Class tu manage all the cryptos

Author : Thomas Vernoux
Date : March 3, 2024
"""

"""
Imports
"""

import json                                  # lib for variables storage management in json files
import time

from global_variables import *               

from functions_crypto import *
from functions_email import *
from functions_basics import *
from functions_peak_detection import *
from functions_CoinBaseApi import *
from functions_log import *


import functions_CoinBaseApi
import functions_basics
import functions_CoinBaseApi



fichier_userfriendly = "user_data_userfriendly.txt"


class Crypto:
    """
    This class is used to manage a crypto account.
    """
    def __init__(self):
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        self.name = None                      # Crypto name on coinbase
        self.coinbaseId = None                # Id for coinbase API
        self.name_cryptocompare = None        # Crypto name on cryptocompare
        self.name_coingecko = None            # Crypto name on coingeko
        self.amount = 0                       # Amount of crypto
        self.last_order_buy_price = 0         # Price I bought this crypto
        self.last_order_buy_datetime = 0      # Time I bought this crypto
        self.max_price = 0                    # Maximum price reached by this crypto
        self.current_price = 0                # Last update price of the crypto
        self.USDC_balance = 0                 # USDC equivalance of the crypto
        self.number_of_alert_authorized = 0   # Number of alerts authorized by this crypto
        self.last_notification_time = 0       # last notification time by this crypto
        self.peak_target = 0                  # % of max value. When reached, send a notification
        self.break_even_point = 0             # % of the cryptocurrency price to be reached to make money
        self.profit_percent = 0               # Profitability
        self.last_buy_order = {}              # Last buy order


    def decrase_number_of_alert_authorized(self):
        """
        This function is used to decrase by 1 the number of alerts authorized. 
        No parameters required
        """
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        self.number_of_alert_authorized -=1    # decrase parameter 
        self.write_variables_to_json_file()    # Write the parameter on json file

    def get_crypto_info_str(self):
        """
        Return crypto info str printable
        """

        log_trace(str(inspect.currentframe().f_back.f_code.co_name) + self.name)

        ret_value = ""

        for key, value in vars(self).items():
            ret_value += str(key) + " " + str(value) + "\n"

        return ret_value

    def sell_for_USDC(self):
        """
        Sell the maximum amount of this crypto for USDC
        """
        
        
        log_trace(str(inspect.currentframe().f_back.f_code.co_name) + self.name)
        log_write("peak detection", str(inspect.currentframe().f_back.f_code.co_name) + self.name)
        order = functions_CoinBaseApi.sell_crypto_for_USDC(self.name)                          # Sell Crypto
        log_write("peak detection", f"order : {str(order)}")
        
        
        
        Variable("extern_change_detected").set(True)                # Change hasbeen detected in crypto accounts
        return(order)

    def initialise_USDC_balance(self): 
        """
        setup the USDC balance for this crypto 
        """

        log_trace(str(inspect.currentframe().f_back.f_code.co_name) + self.name)
        self.current_price = get_price(self)                  # Get price
        self.USDC_balance = self.amount * self.current_price  # USDC balance actualisation

        return True
    
    def write_variables_to_json_file(self):
        """
        Save all crypto classs variables in a json file. Location : CRYPTO json/{self.name}/{self.name}.json
        """
        
        log_trace(str(inspect.currentframe().f_back.f_code.co_name) + self.name)
        folder_path = f"CRYPTO json/{self.name}"               # Path to json folder
        path =  f"CRYPTO json/{self.name}/{self.name}.json"    # Path to json file
        
        if not os.path.exists(folder_path):                    # Detect if the path exist
            os.makedirs(folder_path)                           # Create the folder if the path does not exist
        
        with open(path, 'w') as f:                             # Open json file
            json.dump(self.__dict__, f, indent=4)              # dump all variables

    def get_variables_from_json_file(self):
        """
        This function get all crypto variables from json file
        Actually not use in the code ? 
        """

        log_trace(str(inspect.currentframe().f_back.f_code.co_name) + self.name)
        folder_path = f"CRYPTO json/{self.name}"               # Path to json folder
        path =  f"CRYPTO json/{self.name}/{self.name}.json"    # Path to json file
        
        with open("cryptos.json", "r") as f:
            # Charger le contenu JSON sous forme de liste d'objets Python
            cryptos_data = json.load(f)

    def update_USDC_balance(self):
        """
        Update USDC bamlance using crypto price and crypto amount
        """
        log_trace(str(inspect.currentframe().f_back.f_code.co_name) + self.name)
        try :
            self.USDC_balance = round(self.amount * self.current_price, 2)
        except : 
            log_error_minor(f"Cannot determinate USDC balance (self.USDC_balance = round(self.amount * self.current_price, 2)) for ctypto : {self.get_crypto_info_str()}")
        return

    def update_max_price(self):
        if self.current_price == None :
            log_error_minor("self.current_price == None in update_max_price in class_cryptos.py (Crypto)")
            return
        if self.max_price == None : 
            self.max_price = self.current_price
        
        if self.current_price > self.max_price :
            self.max_price = self.current_price

        self.write_variables_to_json_file()


class CRYPTOS:
    def __init__(self):
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        self.cryptos_list = []

    def getCRYPTO_json(self):
        """
        Get all cryptos info from json
        """
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        self.cryptos_list = []


        folder_path = "CRYPTO json"
        if not(os.path.exists(folder_path)):
            return []
        crypto_list = os.listdir(folder_path)
        for crypto_name in crypto_list :
            crypto_path = f"{folder_path}/{crypto_name}/{crypto_name}.json"
            
            with open(crypto_path, "r") as f:
                # Charger le contenu JSON sous forme de liste d'objets Python
                try :
                    crypto_data = json.load(f)

                    crypto = Crypto()
                    crypto.name = crypto_data.get("name")
                    crypto.coinbaseId = crypto_data.get("coinbaseId")
                    crypto.name_cryptocompare = crypto_data.get("name_cryptocompare")
                    crypto.name_coingecko = crypto_data.get("name_coingecko")
                    crypto.amount = crypto_data.get("amount")
                    crypto.last_order_buy_price = crypto_data.get("last_order_buy_price")
                    crypto.last_order_buy_datetime = crypto_data.get("last_order_buy_datetime")
                    crypto.max_price = crypto_data.get("max_price")
                    crypto.current_price = crypto_data.get("current_price")
                    crypto.USDC_balance = crypto_data.get("USDC_balance")
                    crypto.number_of_alert_authorized = crypto_data.get("number_of_alert_authorized")
                    crypto.last_notification_time = crypto_data.get("last_notification_time")
                    crypto.peak_target = crypto_data.get("peak_target")
                    crypto.break_even_point = crypto_data.get("break_even_point")
                    crypto.profit_percent = crypto_data.get("profit_percent")
                    crypto.last_buy_order = crypto_data.get("last_buy_order")


                    self.cryptos_list.append(crypto)
        
                
                except Exception as e:
                    tb = traceback.format_exc()
                    error_message = f"error in getcrypto_json : {crypto_name}  \n{tb}"
                    print(error_message)
                    log_error_critic(error_message)

        return self.cryptos_list[:]

        
                
    
    def writeCRYPTO_json(self):
        """
        Write all cryptos info to json
        """
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        for c in self.cryptos_list :
            c.write_variables_to_json_file()

    def writeCRYPTO_userfriendly(self):
        """
        Write crypto info in txt file
        """
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        try : 
            cryptos = self.cryptos_list
            with open(fichier_userfriendly, 'w') as f:
                for crypto in cryptos:
                    f.write(f"crypto            : {crypto.name_cryptocompare}\n")
                    f.write(f"ammount           : {crypto.amount}\n")
                    f.write(f"buy price         : {crypto.last_order_buy_price}\n")
                    f.write(f"maximum price     : {crypto.max_price}\n")
                    f.write(f"current price     : {crypto.current_price}\n")
                    f.write(f"USDC_balance      : {crypto.USDC_balance}\n")
                    f.write(f"profit %          : {crypto.profit_percent}\n")
                    f.write(f"alert_ahthorized  : {crypto.number_of_alert_authorized}\n")
                    f.write(f"last notif time   : {int(crypto.last_notification_time)}\n")
                    f.write("\n")
            f.close()
        except Exception as e:
            tb = traceback.format_exc()
            log_error_minor(f"Cannot write in crypto userfriendly: {str(tb)}")

    def cryptos_reset_max_price(self):
        """
        Reset the maximum value of all cryptos to current value
        """
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        cryptos = self.getCRYPTO_json()
        for c in cryptos : 
            c.max_price = c.current_price

        self.writeCRYPTO_json()

    def cryptos_set_notifications_authorisations(self, value):
        """
        Reset the value of all cryptos notifications
        """

        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        cryptos = self.getCRYPTO_json()
        for c in cryptos : 
            c.number_of_alert_authorized = value

        self.writeCRYPTO_json()

    def initialise_all_USDC_balance(self):
        """
        Set the right value of USDC balance, updating cryoto price
        """
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        for c in self.cryptos_list:
            
            c.initialise_USDC_balance()
        self.writeCRYPTO_json()

    def actualise_crypto_account(self):
        """
        refresh crypto account in json file
        """
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        data_api = functions_CoinBaseApi.get_accounts_from_api()


        """
        Set dict ammount api
        """
        dic_amount_api = {}
        for data_C in data_api : 
            
            if data_C["currency"] == "USDC":
                continue
            if data_C["currency"] == "EUR":
                continue
            
            
            amount_str = data_C["available_balance"]["value"]
            amount = float(amount_str)

            dic_amount_api[data_C["currency"]] = amount

        list_of_my_cryptos = []
        for i in self.cryptos_list:
            list_of_my_cryptos.append(i.name)
        

        # Error Check
        for i in range(len(self.cryptos_list)) :
            crypto_name = self.cryptos_list[i].name
            
            if not (crypto_name in dic_amount_api):
                message = "crypto_name is not in dic_price_api : \n" + self.cryptos_list[i].get_crypto_info_str()
                log_write("info", message)
                log_error_minor(message)
                self.cryptos_list[i].amount = 0
                continue
               
        
        for k in dic_amount_api :        # Check if the crypto is in my json file
            
            if k in list_of_my_cryptos : 
                # la crypto de l'api est bien dans mon repertoire json

                # find the correct crypto in the list
                for i in range(len(self.cryptos_list)):
                    if self.cryptos_list[i].name == k:
                        # It is this crypto
                        self.cryptos_list[i].amount = dic_amount_api[self.cryptos_list[i].name]
                    else : continue

            # the Crypto from API is not in my json file (local)
            # Add the crypto
            else : 
                if k == "ETH2":
                    """
                    TODO : debug
                    """
                    # special exception to debug
                    continue
                self.cryptos_list.append(Crypto())
                self.cryptos_list[-1].name = k
                self.cryptos_list[-1].amount = dic_amount_api[self.cryptos_list[-1].name]
                self.cryptos_list[-1].coinbaseId = k
                self.cryptos_list[-1].break_even_point = Variable("break_even_point").get()
                self.cryptos_list[-1].peak_target = 99
                #self.cryptos_list[-1].last_order_buy_price = float(input(f"New crypto detected, please insert buy price for : {k}"))
                Variable("extern_change_detected").set(True)
                log_write("New crypto detected", f"New crypto detected : {str(self.cryptos_list[-1].name)}")

        return

    def set_crypto_peak_target(self, peak_target):
        """
        set variable
        """
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        cryptos = self.getCRYPTO_json()
        for c in cryptos : 
            c.peak_target = peak_target

        self.writeCRYPTO_json()

    def set_crypto_break_even_point(self, break_even_point):
        """
        set variable
        """
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        cryptos = self.getCRYPTO_json()
        for c in cryptos : 
            c.break_even_point = break_even_point

        self.writeCRYPTO_json()

    def set_buy_prices_depreciated(self):
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
        client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
        orders = client.list_orders()

        for c in self.cryptos_list :
            price, time = functions_CoinBaseApi.get_last_buy_price(orders, c)
            c.last_order_buy_price = price
            c.last_order_buy_datetime = time

        
        self.writeCRYPTO_json()
        
        
    def update_last_order_for_each_crypto(self):
        """
        TODO : add this function to the code and also finish it
        """
        log_trace(str(inspect.currentframe().f_back.f_code.co_name))
    
        """
        Find the last order
        """
        for c in self.cryptos_list :
            corresponding_order = functions_CoinBaseApi.get_last_order(c)
            
            if corresponding_order == None :
                None
                #No orders found (possible if you bought the crypto througt eur wallet)
            
            """
            Add the last order to the crypto
            """
            if corresponding_order != None :
                c.last_buy_order = corresponding_order
                c.last_order_buy_price = float(corresponding_order['average_filled_price'])
                c.last_order_buy_datetime = corresponding_order['created_time']
                





