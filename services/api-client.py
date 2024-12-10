# Chamada da API
from config import settings

url = settings.MAKE_URL
token = settings.MAKE_TOKEN
organizationId = settings.MAKE_ORGANIZATION_ID

import requests
import json

url = f"{url}scenarios?organizationId={organizationId}"

payload = {}
headers = {
    f'Authorization': 'Token {token}',
    'Content-Type': 'application/json',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
