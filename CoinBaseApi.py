

from coinbase.rest import RESTClient
import json
import jwt
from cryptography.hazmat.primitives import serialization
import time
import secrets



def load_key_from_json(filename, variable):
    """
    Load a variable from json
    @filename : path to json
    @variable : name of the variable to find in the json
    """
    with open(filename, 'r') as file:
        keys = json.load(file)
    return keys[variable]



key_name = load_key_from_json('coinbase_cloud_api_key.json', "name")
key_secret = load_key_from_json('coinbase_cloud_api_key.json', "privateKey")

request_method = "GET"
request_host   = "api.coinbase.com"
request_path   = "/api/v3/brokerage/accounts"
service_name   = "retail_rest_api_proxy"
def build_jwt(service, uri):
    private_key_bytes = key_secret.encode('utf-8')
    private_key = serialization.load_pem_private_key(private_key_bytes, password=None)
    jwt_payload = {
        'sub': key_name,
        'iss': "coinbase-cloud",
        'nbf': int(time.time()),
        'exp': int(time.time()) + 120,
        'aud': [service],
        'uri': uri,
    }
    jwt_token = jwt.encode(
        jwt_payload,
        private_key,
        algorithm='ES256',
        headers={'kid': key_name, 'nonce': secrets.token_hex()},
    )
    return jwt_token
def main():
    uri = f"{request_method} {request_host}{request_path}"
    jwt_token = build_jwt(service_name, uri)
    print(f"export JWT={jwt_token}")
if __name__ == "__main__":
    main()