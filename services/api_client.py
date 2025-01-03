# Chamada da API
from config import settings
import endpoints
from datetime import datetime

def format_date(iso_date: str) -> str:
    # Converte a string ISO 8601 em um objeto datetime
    dt = datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    # Formata a data no formato desejado
    return dt.strftime("%d/%m/%Y %H:%M")

def linha(txt="-"):
    print(f"{txt:-^50}")

url = settings.MAKE_URL
token = settings.MAKE_TOKEN
organizationId = settings.MAKE_ORGANIZATION_ID

linha("Iniciando Programa!")

# Pega todos os clientes
# Aqui ele gera um dicionário com todos os cenários
res = endpoints.scenarios(url, token, organizationId)
print(f"Total de Cenários: {len(res["scenarios"])}")


# Pega o consumo dos cenários
# Retorna o consumo de cenários que foram utilizados ao menos uma vez
comsumptionCenarios = endpoints.comsumptions(url, token, organizationId)
print(f"Cenários executados desde {format_date(comsumptionCenarios["lastReset"])}: {len(comsumptionCenarios["scenarioConsumptions"])}")


cenariosParados = []
for cenario in comsumptionCenarios["scenarioConsumptions"]:
    if cenario["transfer"] < 50:
        cenariosParados.append(cenario['scenarioId'])

print(f"Cenários sem fluxo de dados: {len(cenariosParados)}")

# linha()
# linha("Cenarios à Excluir:")
# linha()
# 
# for cenario in cenariosParados:
#     for c in res["scenarios"]:
#         if c["id"] == cenario:
#             print(c["name"])

linha()
int(input("""Selecione uma opção:
1 - Gerar Relatório
2 - Desativar Todos
Digite aqui: """))