pip = gerenciador de pacote




---

---
#Soma dois numeros passados como argumentos
def soma(x,y):
  #retorno da funçao
  return x + y

#Resultado Soma
print(soma(50,10))
print(soma(15,20))
print(soma(1050,1200000))

---

def metragem_quadrada(altura_parede,largura_parede):
  mt_quadrado = altura_parede * largura_parede
  print(f'Você tem {mt_quadrado} metros quadrados')

print(metragem_quadrada(2,4))
print(metragem_quadrada(8,16))
print(metragem_quadrada(12,20))

---
#https://geradornv.com.br/gerador-telefone/

def pegar_ddd_telefones(lista_telefones):

  for telefone in lista_telefones:
    ddd = telefone[0:4]
    print(f'O telefone: {telefone} tem o DDD {ddd}')

telefones = ['(86) 3147-7187','(44) 2112-1311','(82) 2573-8537','(15) 2237-8481']
pegar_ddd_telefones(telefones)

---
somar_um = lambda x:x + 1
somar_um(3)

___

#https://www.kaggle.com/datasets/sinhasatwik/salary-base-data/
import pandas as pd
import numpy
import json
import requests
import logging
from datetime import datetime

---

tabela = pd.read_csv('/content/Salary_Data.csv')
#Colunas de uma tabela
print(tabela.columns)

---

#Dados do topo
print(tabela.head())

---
quantidade_linhas = len(tabela)
print(f'Essa tabela tem {quantidade_linhas} linhas')
---
#Dando um aumento de salario de 500 reais para todos os funcionarios
salario_aumento = lambda salario:salario + 500
tabela['Salary'].apply(salario_aumento)
---
#Pega e formata data de hoje
data_hoje = datetime.today().strftime('%d-%m-%Y')
print(data_hoje)
---
#Transforma um texto em uma data
datetime.strptime('2025-01-01','%Y-%m-%d')
---
%pip install emoji
from emoji import emojize
---
for x in range(0,5):
  print(emojize(":thumbs_up:"))
  print(emojize(":blue_heart:"))
  print('\n')
---


class Motor():
  def __init__(self,hp,tipo):
    self.hp = hp
    self.tipo = tipo

  def motor_eletrico(self):
    if self.tipo.upper() == 'ELETRICO':
      return True
    else:
      return False


class Carro(Motor):
  def __init__(self,combustivel,hp,tipo):
    super().__init__(hp,tipo)
    self.hp = hp
    self.tipo = tipo
    self.roda = 4
    self.portas = 2
    self.ar_condicionado = True
    self.volante = True
    self.som = False
    self.motor = None
    self.combustivel = combustivel

  def andar(self):
    if self.combustivel > 0 or self.motor_eletrico():
      print('Andar ')
    else:
      print('Sem combustivel')


Carro(0,400,'eletrico').andar()

