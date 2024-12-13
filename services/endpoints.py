# Retorna todos os cenários, ativos e inativos
import json
import requests

maxLimit = 999999

def formatarDict(j):
    import json
    j = j.text
    return json.loads(j)

def scenarios(url, token, organizationId, limit=maxLimit):
    endpoint = "scenarios"
    url = f"{url}{endpoint}?organizationId={organizationId}&pg[limit]={limit}"

    body = {}
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers, data=body)
    
    return formatarDict(response)



# Retorna o consumo dos cenários que tiveram ao menos uma execução no período
def comsumptions(url, token, organizationId, limit=maxLimit):
    endpoint = "scenarios/consumptions"
    url = f"{url}{endpoint}?organizationId={organizationId}&pg[limit]={limit}"

    body = {}
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers, data=body)

    return formatarDict(response)