

import json
from fonctions_crypto import *
import cryptocompare
import time
from send_email_file import *
from global_variables import *
from function_history import *
from peak_detections_functions import *
from CoinBaseApi import *
from log import *


fichier = "my_cryptos.txt"                                  # TODO : Delete ?
fichier_userfriendly = "user_data_userfriendly.txt"


class Crypto:
    def __init__(self):
        self.name = None                      # Crypto name on coinbase
        self.name_cryptocompare = None        # Crypto name on cryptocompare
        self.name_coingecko = None            # Crypto name on coingeko
        self.amount = 0                       # Amount of crypto
        self.buy_price = 0                    # Price I bought this crypto
        self.max_price = 0                    # Maximum price reached by this crypto
        self.current_price = 0                # Last update price of the crypto
        self.USDC_balance = 0                 # USDC equivalance of the crypto
        self.number_of_alert_authorized = 0   # Number of alerts authorized by this crypto
        self.last_notification_time = 0       # last notification time by this crypto
        self.peak_target = 0                  # % of max value. When reached, send a notification
        self.break_even_point = 0             # % of the cryptocurrency price to be reached to make money

    def decrase_number_of_alert_authorized(self):
        self.number_of_alert_authorized -=1

    def cryptoprocess(self):
        """
        The cryptoprocess functoin process a crypto once.
        The function do the following actions : 
        Print the crypto in term, actaulise crypto value
        Notify by email if necessary 
        """
        

        # simple print
        #print(f"Nom : {crypto.name_cryptocompare}, Amount : {crypto.amount}, Prix d'achat : {crypto.buy_price}, Prix maximum : {crypto.max_price}, Current price : {crypto.current_price}")
        
        # Price actualisation
        if get_variable_mode() == "real":
            self.current_price = get_price(self)
        

        if self.max_price == None : 
            self.max_price = self.current_price
        
        if self.current_price == None : 
            return
        # Max price actualisation
        if self.current_price > self.max_price :
            self.max_price = self.current_price
        
        # USDC balance actualisation
        self.USDC_balance = self.amount * self.current_price
        try : 
            self.profit_percent = self.current_price / self.buy_price * 100
        except : 
            None

        ## peak reset
        if self.current_price < self.buy_price : 
            self.max_price = 0



        ## peak detection
        if peak_detection_O1(self):
        
            """
            Send an email
            """
            subject = "Time to sell alert"
            body = f"{self.name} is {self.peak_target}% of maximum value.\nMax value : {self.max_price}\nCurrent value : {self.current_price}\nBuy price : {self.buy_price}"
            
        
            if get_variable_mode() == "real":
                send_email(subject, body)
            elif get_variable_mode() == "test":
                set_variable_test_mail_send(True)
            
            
            
            # update last notification time
            self.last_notification_time = time.time()
        

        ## save price history in appropriate file
        if get_variable_mode() == "real":
            save_to_file(self)
            



        
        
        
        return self

    def get_crypto_info_str(self):
        """
        Return crypto info str printable
        """

        ret_value = ""

        for key, value in vars(self).items():
            ret_value += str(key) + " " + str(value) + "\n"

        return ret_value





class CRYPTOS:
    def __init__(self):
        self.cryptos_list = []

    def getCRYPTO_old(self):
        with open(fichier, 'r') as f:
            lignes = f.readlines()
        
        cryptos = []
        current_crypto = None

        for i in lignes:
            ligne = i.strip()
            if ligne.startswith("name "):
                if current_crypto:
                    cryptos.append(current_crypto)
                current_crypto = Crypto()
                current_crypto.name  = ligne.split(":")[1].strip()
            elif ligne.startswith("name_cryptocompare"):
                current_crypto.name_cryptocompare = ligne.split(":")[1].strip()
            elif ligne.startswith("name_coingecko"):
                current_crypto.name_coingecko = ligne.split(":")[1].strip()
            elif ligne.startswith("amount"):
                current_crypto.amount = float(ligne.replace(",", ".").split(":")[1].strip())
            elif ligne.startswith("buy_price"):
                current_crypto.buy_price = float(ligne.replace(",", ".").split(":")[1].strip())
            elif ligne.startswith("max_price"):
                current_crypto.max_price = float(ligne.replace(",", ".").split(":")[1].strip())
            elif ligne.startswith("current_price"):
                current_crypto.current_price = float(ligne.replace(",", ".").split(":")[1].strip())
            elif ligne.startswith("USDC_balance"):
                current_crypto.USDC_balance = float(ligne.replace(",", ".").split(":")[1].strip())
            elif ligne.startswith("profit %"):
                current_crypto.profit_percent = float(ligne.replace(",", ".").split(":")[1].strip())
            elif ligne.startswith("number_of_alert_authorized"):
                current_crypto.number_of_alert_authorized = int(ligne.replace(",", ".").split(":")[1].strip())
            elif ligne.startswith("last_notification_time"):
                current_crypto.last_notification_time = float(ligne.replace(",", ".").split(":")[1].strip())
            elif ligne.startswith("peak_target"):
                current_crypto.peak_target = float(ligne.replace(",", ".").split(":")[1].strip())
            elif ligne.startswith("break_even_point"):
                current_crypto.break_even_point = float(ligne.replace(",", ".").split(":")[1].strip())
        # Ajoutez la dernière crypto après la boucle
        if current_crypto:
            cryptos.append(current_crypto)

    
        self.cryptos_list = cryptos[:]
        return cryptos

    def getCRYPTO_json(self):

        cryptos_data = []

        

        # Ouvrir le fichier JSON en mode lecture
        with open("cryptos.json", "r") as f:
            # Charger le contenu JSON sous forme de liste d'objets Python
            cryptos_data = json.load(f)


        cryptos_list = []
        for crypto_data in cryptos_data:
            crypto = Crypto()
            crypto.name = crypto_data.get("name")
            crypto.name_cryptocompare = crypto_data.get("name_cryptocompare")
            crypto.name_coingecko = crypto_data.get("name_coingecko")
            crypto.amount = crypto_data.get("amount")
            crypto.buy_price = crypto_data.get("buy_price")
            crypto.max_price = crypto_data.get("max_price")
            crypto.current_price = crypto_data.get("current_price")
            crypto.USDC_balance = crypto_data.get("USDC_balance")
            crypto.number_of_alert_authorized = crypto_data.get("number_of_alert_authorized")
            crypto.last_notification_time = crypto_data.get("last_notification_time")
            crypto.peak_target = crypto_data.get("peak_target")
            crypto.break_even_point = crypto_data.get("break_even_point")
            
            if not (isinstance(crypto.buy_price, float) or crypto.buy_price == 0):
                crypto.buy_price = -1

            if not (isinstance(crypto.current_price, float) or crypto.current_price == 0):
                crypto.current_price = -1

            if not (isinstance(crypto.max_price, float) or crypto.max_price == 0):
                crypto.max_price = -1
            
                



            cryptos_list.append(crypto)
        

            self.cryptos_list = cryptos_list[:]
        return cryptos_list

    def writeCRYPTO_old(cryptos):
        with open(fichier, 'w') as f:
            for crypto in cryptos:
                for key, value in crypto.__dict__.items():
                    f.write(f"{key} : {value}\n")
                f.write("\n")
        f.close()
        return
    
    def writeCRYPTO_json(self):
        a = self.cryptos_list
        with open("cryptos.json", 'w') as f:
            json.dump([crypto.__dict__ for crypto in self.cryptos_list], f, indent=4)

    def writeCRYPTO_userfriendly(self):
        cryptos = self.cryptos_list
        with open(fichier_userfriendly, 'w') as f:
            for crypto in cryptos:
                f.write(f"crypto            : {crypto.name_cryptocompare}\n")
                f.write(f"ammount           : {crypto.amount}\n")
                f.write(f"buy price         : {crypto.buy_price}\n")
                f.write(f"maximum price     : {crypto.max_price}\n")
                f.write(f"current price     : {crypto.current_price}\n")
                f.write(f"USDC_balance      : {crypto.USDC_balance}\n")
                f.write(f"profit %          : {crypto.profit_percent}\n")
                f.write(f"alert_ahthorized  : {crypto.number_of_alert_authorized}\n")
                f.write(f"last notif time   : {int(crypto.last_notification_time)}\n")
                f.write("\n")
        f.close()

    def cryptos_reset_max_price(self):
        """
        Reset the maximum value of all cryptos to current value
        """

        cryptos = self.getCRYPTO_json()
        for c in cryptos : 
            c.max_price = c.current_price

        self.writeCRYPTO_json()

    def cryptos_set_notifications_authorisations(self, value):
        """
        Reset the value of all cryptos notifications
        """

        cryptos = self.getCRYPTO_json()
        for c in cryptos : 
            c.number_of_alert_authorized = value

        self.writeCRYPTO_json()

    def actualise_crypto_account(self):
        """
        refresh crypto account in json file
        """
        data_api = get_accounts_from_api()["data"]
        #print(data)
        dic_price_api = {}
        for data_C in data_api : 
            dic_price_api[data_C["balance"]["currency"]] = float(data_C["balance"]["amount"])

        #print (dic_price_api)
        list_of_my_cryptos = []
        for i in range(len(self.cryptos_list)) :
            crypto_name = self.cryptos_list[i].name
            
            # Error check
            if not (crypto_name in dic_price_api):
                minor_error("crypto_name is not in dic_price_api : \n" + self.cryptos_list[i].get_crypto_info_str())
                self.cryptos_list[i].amount = 0
                continue

            try :
                list_of_my_cryptos.append(crypto_name)
                self.cryptos_list[i].amount = dic_price_api[crypto_name]
            except : 
                minor_error("ammount refresh error : \n" + self.cryptos_list[i].get_crypto_info_str())

        for k in dic_price_api :
            if k in list_of_my_cryptos :
                # la crypto de l'api est bien dans mon repertoire json
                continue
            else : 
                # On cree la crypto qui manque
                for i in self.cryptos_list :
                    print("crypto list _ name : ", i.name)
                #a = self.cryptos_list[:]
                self.cryptos_list.append(Crypto())
                #a = self.cryptos_list[:]
                print(k)
                self.cryptos_list[-1].name = k
                self.cryptos_list[-1].amount = dic_price_api[k]
                



        self.writeCRYPTO_json()




    




    











