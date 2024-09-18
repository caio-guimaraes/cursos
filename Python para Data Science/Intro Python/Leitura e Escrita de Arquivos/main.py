import csv
import os
import produto

def verificar_arquivo(): 
   caminho = 'arquivos/produto' 
   arquivo = caminho + '/dados.csv'

   if not os.path.exists(caminho): 
      os.makedirs(caminho)
   elif not os.path.isdir(caminho):
      raise IOError(caminho + " nao é um diretorio!")

   if not os.path.exists(arquivo): 
      open(arquivo, 'w')

   return arquivo

def ler_produtos(arquivo):
   arquivo_aberto = open(arquivo, 'r')
   return csv.reader(arquivo_aberto,delimiter=',')

arquivo = verificar_arquivo()
dados = ler_produtos(arquivo)
print(type (dados))

produtos = []

next(dados)
for dado in dados:
   print(dado)
   produtos.append(produto.Produto(dado[0], dado[1]))

print(produtos)
