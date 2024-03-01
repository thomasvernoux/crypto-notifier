# run with python 3.10



import cryptocompare


KEY = "54f504ee770c3ce7a29db71a6e8b17ecbc8e71e18712fc5dd9c4341f6f89fe22"

cryptocompare.cryptocompare._set_api_key_parameter(KEY)
price = cryptocompare.get_price('BTC', 'USD')
print("price : ", price["BTC"]["USD"])
