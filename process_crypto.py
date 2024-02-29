from fonctions_crypto import *
import cryptocompare



CRYPTOS = getCRYPTO()


for crypto in CRYPTOS:
    print()
    #print(f"Nom : {crypto.name}, Amount : {crypto.amount}, Prix d'achat : {crypto.buy_price}, Prix maximum : {crypto.max_price}")
    #current_price = cryptocompare.get_price(crypto.name, 'USD')
    #print(current_price)
