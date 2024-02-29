

class Crypto:
    def __init__(self, name, amount, buy_price, max_price):
        self.name = name
        self.amount = amount
        self.buy_price = buy_price
        self.max_price = max_price

# Création d'une instance de la classe Crypto
crypto_instance = Crypto("Bitcoin", 1.0, 40000, 60000)

# Parcours des valeurs des attributs de l'instance de la classe Crypto
for key, value in crypto_instance.__dict__.items():
    print(f"{key}: {value}")

    