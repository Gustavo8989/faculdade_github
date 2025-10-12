from datetime import datetime
import pandas as pd
import random 
import re


class Produto:
    def __init__(self,produto:str,preco:int,avaliacao:float,data_adicao:datetime,categoria:str):       
        self.produto = produto 
        self.preco = preco 
        self.avaliacao = avaliacao 
        self.data_adicao = data_adicao 
        self.categoria = categoria 
        dados = {"Data": self.data_adicao,
                     "Produto":self.produto,
                     "Preço":self.preco,
                     "Categoria":self.categoria,
                     "Avaliação":self.avaliacao}
        self.table = pd.DataFrame(dados)

  #Algoritmo de Bubble Sort com os dados organizados em ordem cresente
    def bubble_sort(self):
        tamanho = len(self.table)

    def get_info(self):
        print(self.table)



produto = [] 
valores = []
data = []
avaliacao = [] 
categoria_ = [f"Categoria {c+1}" for c in range(20)]
categoria = []
#random_number = [c for c in range(100) categoria.append(f"Categoria {c}")]

for c in range(1000):
    ano = random.randint(2020,2025)
    mes = random.randint(1,12)
    dia = random.randint(1,28)
    produto.append(f"produto {c}")
    valores.append(round(random.uniform(0,1000),2))
    data.append(datetime(ano,mes,dia))
    avaliacao.append(random.randint(0,5))
    categoria.append(random.choice(categoria_))

teste = Produto(produto,valores,avaliacao,data,categoria)
teste.get_info()