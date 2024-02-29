class Crypto:
    def __init__(self):
        self.name = None
        self.amount = None
        self.buy_price = None
        self.max_price = None
        self.current_price = None
        self.USDC_balance = None
        self.number_of_alert_authorized = 0
        self.last_notification_time = 0



fichier = "user_data.txt"

def getCRYPTO():
    with open(fichier, 'r') as f:
        lignes = f.readlines()
    
    cryptos = []
    current_crypto = None

    for i in lignes:
        ligne = i.strip()
        if ligne.startswith("crypto"):
            if current_crypto:
                cryptos.append(current_crypto)
            current_crypto = Crypto()
            current_crypto.name = ligne.split(":")[1].strip()
        elif ligne.startswith("ammount"):
            current_crypto.amount = float(ligne.split(":")[1].strip())
        elif ligne.startswith("buy price"):
            current_crypto.buy_price = float(ligne.split(":")[1].strip())
        elif ligne.startswith("maximum price"):
            current_crypto.max_price = float(ligne.split(":")[1].strip())
        elif ligne.startswith("current price"):
            current_crypto.current_price = float(ligne.split(":")[1].strip())
        elif ligne.startswith("USDC balance"):
            current_crypto.USDC_balance = float(ligne.split(":")[1].strip())
        elif ligne.startswith("profit %"):
            current_crypto.profit_percent = float(ligne.split(":")[1].strip())
        elif ligne.startswith("alert_ahthorized"):
            current_crypto.number_of_alert_authorized = int(ligne.split(":")[1].strip())
        elif ligne.startswith("last notif time"):
            current_crypto.last_notification_time = int(ligne.split(":")[1].strip())
    # Ajoutez la dernière crypto après la boucle
    if current_crypto:
        cryptos.append(current_crypto)

    for i in cryptos :
        print("i", i)

    return cryptos

def writeCRYPTO(cryptos):
    with open(fichier, 'w') as f:
        for crypto in cryptos:
            f.write(f"crypto            : {crypto.name}\n")
            f.write(f"ammount           : {crypto.amount}\n")
            f.write(f"buy price         : {crypto.buy_price}\n")
            f.write(f"maximum price     : {crypto.max_price}\n")
            f.write(f"current price     : {crypto.current_price}\n")
            f.write(f"USDC_balance      : {crypto.USDC_balance}\n")
            f.write(f"profit %          : {crypto.profit_percent}\n")
            f.write(f"alert_ahthorized  : {crypto.number_of_alert_authorized}\n")
            f.write(f"last notif time   : {int(crypto.last_notification_time)}\n")
            f.write("\n")

