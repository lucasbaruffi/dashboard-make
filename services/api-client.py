# Chamada da API
from config import settings
import endpoints

url = settings.MAKE_URL
token = settings.MAKE_TOKEN
organizationId = settings.MAKE_ORGANIZATION_ID

# Pega todos os clientes
# Aqui ele gera um dicionário com todos os cenários
res = endpoints.scenarios(url, token, organizationId, 1)

# Pega o consumo dos cenários
# Retorna o consumo de cenários que foram utilizados ao menos uma vez
comsumptionCenarios = endpoints.comsumptions(url, token, organizationId)

