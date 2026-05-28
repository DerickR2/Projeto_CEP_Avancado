""""
Arquivo com as ferramentas de comunicação com APIs
"""

import requests

def buscar_cep(cep: str) -> dict:
    """
    A função recebe um cep, consulta uma API e devolve informações sobre o cep.
    """
    resposta = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}", timeout=10)
    return resposta.json()

print(buscar_cep("06501115"))