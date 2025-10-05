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
        self.table = {"Data": data_adicao,
                     "Produto":produto,
                     "Preço":preco,
                     "Categoria":categoria,
                     "Avaliação":avaliacao}

    #Algoritmo de Bubble Sort com os dados organizados em ordem cresente
    def bubble_sort(self):
        tamanho = len(self.table)




produto = [] 
valores = []
data = []
avaliacao = [] 
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
    if c < 20:
        categoria.append(f"Categoria {c}")

teste = Produto(produto,valores,data,categoria,avaliacao)
