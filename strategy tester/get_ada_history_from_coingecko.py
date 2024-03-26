

import requests

def download_price_history_to_csv():
    url = "https://api.coingecko.com/api/v3/coins/cardano/market_chart?vs_currency=usd&days=365&interval=daily"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open("ada_price_history.json", "wb") as f:
            f.write(response.content)
        print("Download successful. Data saved to ada_price_history.csv")
    else:
        print("Failed to download data.")

# Appel de la fonction pour télécharger les données historiques sur les prix de Cardano
download_price_history_to_csv()


