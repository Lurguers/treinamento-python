import json
from time import sleep
import requests
from funcoes import consultar

resultado = consultar("""
            select * from bethadba.pessoas p inner join bethadba.pessoas_fisicas pf on (p.i_pessoas = pf.i_pessoas) where p.i_pessoas = 1
""")
listaLotes = []
for i in resultado:
    # print(i)
    sexo = None
    if i['sexo'] == "M":
        sexo = 'MASCULINO'
    else:
        sexo = 'FEMININO'
    # print(i['sexo'])
    dado = {
        'nome': i['nome'].strip(),
        'dataNascimento': i['dt_nascimento'].strftime("%Y-%m-%d"),
        'cpf': i['cpf'],
        'sexo': sexo,
        'tipoPessoa': 'FISICA',
        'inicioVigencia': '2022-04-21 19:12:13'
    }
    url = 'https://pessoal.cloud.betha.com.br/service-layer/v1/api/pessoa/'
    lote = json.dumps([{
        'idIntegracao': 'teste de treinamento 2',
        'conteudo': dado
    }])
    print(lote)
    cabecalho = {
        'Authorization': 'Bearer c6171025-a595-45c1-9dbe-55b28e39622d',
        'Content-Type': 'application/json'
    }
    resposta = requests.request("POST", url, headers=cabecalho, data=lote)
    resposta = resposta.json()

    if 'id' in resposta:
        listaLotes.append(resposta['id'])
    else:
        print(f"Deu erro!!!! {resposta['message']}")

print(listaLotes)

for k in listaLotes:
    situacao = 'AGUARDANDO_EXECUCAO'

    while situacao in ('AGUARDANDO_EXECUCAO', 'EXECUTANDO'):
        url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/lote/lotes/{k}'

        lote = {}

        cabecalho = {
            'Authorization': 'Bearer c6171025-a595-45c1-9dbe-55b28e39622d',
            'Content-Type': 'application/json'
        }

        resposta = requests.request("GET", url, headers=cabecalho, data=lote)
        resposta = resposta.json()
        situacao = resposta['situacao']
        # print(situacao)
        sleep(2)
    print(resposta['retorno'][0]['situacao'])
    if resposta['retorno'][0]['mensagem']:
        print(resposta['retorno'][0]['mensagem'])