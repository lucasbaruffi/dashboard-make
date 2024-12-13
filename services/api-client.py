# Chamada da API
from config import settings
import endpoints
import json

url = settings.MAKE_URL
token = settings.MAKE_TOKEN
organizationId = settings.MAKE_ORGANIZATION_ID

res = endpoints.scenarios(url, token, organizationId, 1)
res = json.loads(res)


for cenario in res["scenarios"]:
    print(cenario)
    id = cenario["id"]
    name = cenario["name"]
   # folder = cenario["folder"]


    print(f"{id} - {name}")


#for c in res["scenarios"]:
 #   print(res["scenarios"][c]["id"])