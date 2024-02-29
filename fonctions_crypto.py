class Crypto:
    def __init__(self):
        self.name = None
        self.amount = None
        self.buy_price = None
        self.max_price = None
        self.current_price = None
        USDC_balance = None


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
    # Ajoutez la dernière crypto après la boucle
    if current_crypto:
        cryptos.append(current_crypto)

    for i in cryptos :
        print("i", i)

    return cryptos

def writeCRYPTO(cryptos):
    with open(fichier, 'w') as f:
        for crypto in cryptos:
            f.write(f"crypto : {crypto.name}\n")
            f.write(f"ammount : {crypto.amount}\n")
            f.write(f"buy price : {crypto.buy_price}\n")
            f.write(f"maximum price : {crypto.max_price}\n")
            f.write(f"current price : {crypto.current_price}\n")
            f.write(f"USDC_balance : {crypto.USDC_balance}\n")
            f.write("\n")

