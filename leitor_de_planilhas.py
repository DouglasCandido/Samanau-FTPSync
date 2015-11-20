# Author: Douglas Cândido
# coding: utf-8

import xlrd

nome_arquivo = input("Digite o nome do arquivo com a extensao .xlsx que voce quer ler:")

xlsx = xlrd.open_workbook(nome_arquivo)
planilha = xlsx.sheets()[0]

for linha in xrange(planilha.nrows):
    print planilha.row_values(linha)






