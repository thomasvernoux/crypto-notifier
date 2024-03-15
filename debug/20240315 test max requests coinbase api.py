






from coinbase.rest import RESTClient


product_id = f"AVT-USDC"
USDC_sty = "2.000"




client = RESTClient(key_file="api_keys/coinbase_cloud_api_key V2.json")

for i in range (100):
    product = client.get_product(product_id)
    print(product)







