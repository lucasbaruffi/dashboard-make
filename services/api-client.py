# Chamada da API
from config import settings
import endpoints

url = settings.MAKE_URL
token = settings.MAKE_TOKEN
organizationId = settings.MAKE_ORGANIZATION_ID

res = endpoints.scenarios(url, token, organizationId, 1)
res = dict(res)
for c in res["scenarios"]:
    print(res["scenarios"]["id"])