from fonctions_crypto import *
import cryptocompare



CRYPTOS = getCRYPTO()


for crypto in CRYPTOS:
    print()
    print(f"Nom : {crypto.name}, Amount : {crypto.amount}, Prix d'achat : {crypto.buy_price}, Prix maximum : {crypto.max_price}, Current price : {crypto.current_price}")
    current_price = cryptocompare.get_price(crypto.name, 'USD')
    if crypto.current_price > crypto.max_price :
        crypto.max_price = crypto.current_price
    crypto.USDC_balance = crypto.amount * crypto.current_price

writeCRYPTO(CRYPTOS)
