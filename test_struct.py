
from fonctions_crypto import *

# Utilisation du script
fichier = "user_data.txt"  # Mettez le nom de votre fichier ici
CRYPTOS = getCRYPTO()
writeCRYPTO(CRYPTOS)

for crypto in CRYPTOS:
    print(f"Nom : {crypto.name}, Amount : {crypto.amount}, Prix d'achat : {crypto.buy_price}, Prix maximum : {crypto.max_price}")
