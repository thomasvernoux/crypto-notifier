
import sys
sys.path.append('./')

from coinbase.rest import RESTClient

client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")
#accounts = client.get_accounts()


product_id = "AUCTION-USDC"
#available_sell_quantity = "0.36859257640732"
#available_sell_quantity = "0.368"

available_sell_quantity = "3.6e-1"


order = client.preview_market_order_sell(product_id = product_id, base_size = available_sell_quantity)

print(order)

