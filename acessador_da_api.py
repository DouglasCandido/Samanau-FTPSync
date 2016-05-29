# -*- coding: utf-8 -*-

# import json
import requests
import string

# Informações retornadas pela requisição
def info(requisicao): 
	print "Codigo: " + str(requisicao.status_code) + "\n"
	print "Content-type: " + requisicao.headers['content-type'] + "\n"
	# print "Conteudo retornado: " + requisicao.content + "\n"
	# print "Texto retornado: " + requisicao.text + "\n"
	print "Json Retornado: " + str(requisicao.json()) + "\n \n"

requisicao = requests.get('http://samanau.ifrn.edu.br/api/v1/')
info(requisicao)

# Requisição para se autenticar e pegar o token de acesso da API
autenticacao = {'username':'ccslcaico', 'password':'ccsl123'}

requisicao = requests.post('http://samanau.ifrn.edu.br/api/v1/token/'
, autenticacao)
info(requisicao)

conteudo_retornado = requisicao.json()
# token = conteudo_retornado['token']
token = str(conteudo_retornado['token'])

# Requisição para cadastrar uma nova estação
devices = ['1', '2', '3', '4', '5', '6', '7']

autenticacao_token = {'Authorization': 'Token 0b52e642a07e06f99942d97cf0e2d0cd0ad1b501'}

parametros = {'firmware_id':1, 'devices':devices}
# parametros = {'firmware_id':1, 'devices':devices}

parametros.update(autenticacao_token)

requisicao = requests.post('http://samanau.ifrn.edu.br/api/v1/station/', headers = parametros)
info(requisicao)

# Requisição para salvar os dados coletados



