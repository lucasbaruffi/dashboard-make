# Retorna todos os cenários, ativos e inativos
def scenarios(url, token, organizationId, limit=10000):
    import requests
    endpoint = "scenarios"
    url = f"{url}{endpoint}?organizationId={organizationId}&pg[limit]={limit}"

    body = {}
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers, data=body)

    return response.text

# Retorna o consumo dos cenários que tiveram ao menos uma execução no período
def comsumptions(url, token, organizationId):
    import requests
    endpoint = "scenarios/consumptions"
    url = f"{url}{endpoint}?organizationId={organizationId}"

    body = {}
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers, data=body)

    return response.text