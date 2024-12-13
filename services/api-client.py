# Chamada da API
from config import settings
import endpoints
import json

url = settings.MAKE_URL
token = settings.MAKE_TOKEN
organizationId = settings.MAKE_ORGANIZATION_ID

# Pega todos os clientes
#res = endpoints.scenarios(url, token, organizationId, 1)

# Aqui ele gera um dicionário com todos os cenários
#allCenarios = json.loads(res)




comsumptionCenarios = endpoints.comsumptions(url, token, organizationId)
print(comsumptionCenarios)

# for cenario in totClientes["scenarios"]:
#     print(cenario)
#     id = cenario["id"]
#     name = cenario["name"]
#    # folder = cenario["folder"]
# 
# 
#     print(f"{id} - {name}")


# for c in res["scenarios"]:
#    print(res["scenarios"][c]["id"])