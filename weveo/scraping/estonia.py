from bs4 import BeautifulSoup
import requests
import json


headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
}

# CONSUMER PRICE INDEX, CHANGE (Months)

url_api = "https://andmed.stat.ee/api/v1/en/stat?query=Consumer%20price%20index" 

# Realizar la solicitud GET con el query como parámetro de consulta
response = requests.get(url_api)

if response.status_code == 200:
    json_result = response.json()
    print(json_result)
else:
    print("Error:", response.status_code)

