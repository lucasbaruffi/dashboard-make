
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