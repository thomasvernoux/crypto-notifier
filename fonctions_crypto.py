class Crypto:
    def __init__(self):
        self.name = None
        self.amount = None
        self.buy_price = None
        self.max_price = None

def lire_fichier(fichier):
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
    # Ajoutez la dernière crypto après la boucle
    if current_crypto:
        cryptos.append(current_crypto)

    for i in cryptos :
        print("i", i)

    return cryptos

def ecrire_fichier(cryptos, fichier_sortie):
    with open(fichier_sortie, 'w') as f:
        for crypto in cryptos:
            f.write(f"crypto : {crypto.name}\n")
            f.write(f"ammount : {crypto.amount}\n")
            f.write(f"buy price : {crypto.buy_price}\n")
            f.write(f"maximum price : {crypto.max_price}\n")
            f.write("\n")

