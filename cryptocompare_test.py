# run with python 3.10

import cryptocompare
price = cryptocompare.get_price('BTC', 'USD')
print(price)

