import requests

def api_moeda():
    response = requests.get("https://v6.exchangerate-api.com/v6/44d6878ce80641a9ce9ee3eb/latest/USD", timeout=5)
    return response.json()
