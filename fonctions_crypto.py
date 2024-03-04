
import time
from global_variables import *
import cryptocompare
from pycoingecko import CoinGeckoAPI
import traceback



time_notif_interval = 10 * 60  # interval between 2 notofications : 10 min

fichier = "my_cryptos.txt"
fichier_userfriendly = "user_data_userfriendly.txt"


class Crypto:
    def __init__(self):
        self.name = None                      # Crypto name
        self.name_cryptocompare = None        # Crypto name on cryptocompare
        self.name_coingecko = None          # Crypto name on coingeko
        self.amount = None                    # Amount of crypto
        self.buy_price = None                 # Price I bought this crypto
        self.max_price = None                 # Maximum price reached by this crypto
        self.current_price = None             # Last update price of the crypto
        self.USDC_balance = None              # USDC equivalance of the crypto
        self.number_of_alert_authorized = 0   # Number of alerts authorized by this crypto
        self.last_notification_time = 0       # last notification time by this crypto
        self.peak_target = 0                  # % of max value. When reached, send a notification
        self.break_even_point = 0             # % of the cryptocurrency price to be reached to make money

    def decrase_number_of_alert_authorized(self):
        self.number_of_alert_authorized -=1


def getCRYPTO():
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

    

    return cryptos

def writeCRYPTO(cryptos):
    with open(fichier, 'w') as f:
        for crypto in cryptos:
            for key, value in crypto.__dict__.items():
                f.write(f"{key} : {value}\n")
            f.write("\n")
    f.close()
            
def writeCRYPTO_userfriendly(cryptos):
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

def time_interval(crypto):
    """
    Check time intervall between two notification requests
    retrn true or false if the notification can be done
    """
    if (time.time() > crypto.last_notification_time + time_notif_interval) or (crypto.last_notification_time == 0):
        return True
    return False

def get_crypto_price_cryptocompare(crypto):
    """
    Get price from cryptocompare API
    """

    # Ouvrez le fichier contenant le compteur
    with open("api_counter/counter_cryptocompare.txt", "r+") as file:
        count = int(file.read() or 0)  # Lisez le compteur actuel ou initialisez-le à zéro
        count += 1  # Incrémentez le compteur
        file.seek(0)  # Déplacez le curseur au début du fichier
        file.write(str(count))  # Écrivez le nouveau compteur dans le fichier
        file.truncate()  # Tronquez le fichier au cas où le nouveau compteur est plus court que l'ancien


    return cryptocompare.get_price(crypto.name_cryptocompare, 'USD')[crypto.name_cryptocompare]["USD"]

def get_crypto_price_coingecko(crypto):
    """
    Get price from coingecko api

    Is CoinGecko API free?
    CoinGecko API offers both free and paid plans. 
    The Demo API plan is accessible to all CoinGecko users at zero cost, 
    with a stable rate limit of 30 calls/min and a monthly cap of 10,000 calls.

    = 13 calls per hours
    """
    # compteur d'utilisation de l'api pygecko
    # Ouvrez le fichier contenant le compteur
    with open("api_counter/counter_coingecko.txt", "r+") as file:
        count = int(file.read() or 0)  # Lisez le compteur actuel ou initialisez-le à zéro
        count += 1  # Incrémentez le compteur
        file.seek(0)  # Déplacez le curseur au début du fichier
        file.write(str(count))  # Écrivez le nouveau compteur dans le fichier
        file.truncate()  # Tronquez le fichier au cas où le nouveau compteur est plus court que l'ancien



    cg = CoinGeckoAPI()
    return cg.get_price(ids=crypto.name_coingecko, vs_currencies='usd')[crypto.name_coingecko]["usd"]

def get_price(crypto):
    """
    Get price :
    try to use coingecko to get the price, if it is not possible, try with cryptocompare
    """

    price = None
    try :
        price = get_crypto_price_coingecko(crypto)
    except Exception : 
        print ("coingecko error")
        traceback.print_exc()


    try : 
            price = get_crypto_price_cryptocompare(crypto)
    except Exception: 
        print ("cryptocompare error")
        traceback.print_exc()
    if price != None :
        return price
    else:
        while 1 : 
            print("error getting price")
            time.sleep (3)

def cryptos_reset_max_price():
    """
    Reset the maximum value of all cryptos to current value
    """

    cryptos = getCRYPTO()
    for c in cryptos : 
        c.max_price = c.current_price

    writeCRYPTO(cryptos)
    
def cryptos_set_notifications_authorisations(value):
    """
    Reset the value of all cryptos notifications
    """

    cryptos = getCRYPTO()
    for c in cryptos : 
        c.number_of_alert_authorized = value

    writeCRYPTO(cryptos)

