import json
from time import sleep

import requests

limit = 10
offset = 0
pagina = 0
hasNext = True
listaAlterar = []

while hasNext:
    url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/pessoa?limit={limit}&offset={offset}'
    lote = {}
    cabecalho = {
            'Authorization': 'Bearer c6171025-a595-45c1-9dbe-55b28e39622d'
    }

    resposta = requests.request("GET",url, headers=cabecalho, data=lote)
    resposta = resposta.json()
    # print(resposta)
    pagina = pagina + 1
    offset = limit * pagina
    hasNext = resposta['hasNext']

    for i in resposta['content']:
        # print(i)
        if 'nome' in i and i['nome'] == 'EMANUEL DE MELO ALEXANDRE':
            listaAlterar.append(i)


print(listaAlterar)
listaLotes = []
for j in listaAlterar:
    url = 'https://pessoal.cloud.betha.com.br/service-layer/v1/api/historico-pessoa/'

    j['estadoCivil'] = 'DIVORCIADO'
    j.pop('version')
    lote = json.dumps([{
        'idIntegracao': 'teste de treinamento',
        'conteudo': j
    }])
    cabecalho = {
        'Authorization': 'Bearer c6171025-a595-45c1-9dbe-55b28e39622d',
        'Content-Type': 'application/json'
    }
    resposta = requests.request("POST",url, headers=cabecalho,data=lote)
    resposta = resposta.json()

    if 'id' in resposta:
        listaLotes.append(resposta['id'])
    else:
        print(f"Deu erro!!!! {resposta['message']}")

print(listaLotes)

for k in listaLotes:
    situacao = 'AGUARDANDO_EXECUCAO'

    while situacao in ('AGUARDANDO_EXECUCAO','EXECUTANDO'):
        url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/lote/lotes/{k}'

        lote = {}

        cabecalho = {
            'Authorization': 'Bearer c6171025-a595-45c1-9dbe-55b28e39622d',
            'Content-Type': 'application/json'
        }

        resposta = requests.request("GET", url, headers=cabecalho, data=lote)
        resposta = resposta.json()
        # situacao = resposta['situacao']
        # print(situacao)
        # sleep(2)
    print(resposta['retorno'][0]['situacao'])
    print(resposta['retorno'][0]['mensagem'])