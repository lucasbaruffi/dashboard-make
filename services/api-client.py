# Chamada da API
from config import settings
import endpoints
import json

url = settings.MAKE_URL
token = settings.MAKE_TOKEN
organizationId = settings.MAKE_ORGANIZATION_ID

res = endpoints.scenarios(url, token, organizationId, 2)
res = json.loads(res)


for cenario in res["scenarios"]:
    print(cenario["id"])


#for c in res["scenarios"]:
 #   print(res["scenarios"][c]["id"])