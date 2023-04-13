import requests
import json

def get_exchange_rate():
    api_key = "YOUR_API_KEY"
    base_url = "https://openexchangerates.org/api/latest.json?app_id=" + api_key
    response = requests.get(base_url)
    if response.status_code == 200:
        data = json.loads(response.text)
        usd_rate = data["rates"]["USD"]
        eur_rate = data["rates"]["EUR"]
        exchange_rate = eur_rate / usd_rate
        return {"exchange_rate": exchange_rate}
    else:
        return {"error": "Unable to retrieve exchange rate."}

print(get_exchange_rate())