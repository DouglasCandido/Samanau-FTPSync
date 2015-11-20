# Author: Douglas Cândido
# coding: utf-8

import json
import requests

api = input("Digite o endereço de acesso da API:")

requisicao = requests.get(api)

if requisicao.status_code == 200:
    dados = json.loads(requisicao.content)


