import datetime
import random 


class Produto:
    def __init__(self,datas:datetime.datetime,produto:str,preco:int,avaliacao:float,categoria:str):       
        self.produto = produto 
        self.preco = preco 
        self.avaliacao = avaliacao 
        self.datas = datas 
        self.categoria = categoria 

    def __repr__(self):
        return f"{self.produto}: {self.preco}, {self.avaliacao}, {self.datas}, {self.categoria}"
   

def gerando_dados(n):
    nome = ["Produtos " + str(c) for c in range(n)]
    preco = [round(random.uniform(0,1000),2) for c in range(n)]
    avaliacao = [round(random.uniform(0,5),2) for _ in range(n)]
    datas = [datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365)) for _ in range(n)]
    categoria = ["Categoria: " + str(random.randint(0,5)) for c in range(n)]
    produto = [Produto(datas[i],nome[i], preco[i], avaliacao[i],categoria[i]) for i in range(n)]
    return produto

produtos = gerando_dados(1000)
n = len(produtos)
def visualizar():
    for produto in produtos:
        print(produto)

# Valor 
def buble_sort():
    for c in range(n):
        # Esta percorendo a lista inteira proporcional a quantidade de itens, Nesse caso a lista vai se repetir 1000 vezes 
        for k in range(0, n-c-1):
            # Verificando se o numero é maior ou menos
            if produtos[k].preco > produtos[k+1].preco:
                # Trocando de lugar
                pass 

# Avaliação
def QuickSort():
    pivo = int(len(produtos)) // 2
    maior = []
    menor = []
    for c in range(n):
        if pivo > c:
            menor.append(c)
        elif pivo < c:
            maior.append(c)
    # Modificar a lista produtos 

# Data
def MargeSort():
    # Separar a lista em varias partes menores até ficar com os valores unicos 
    meio = n // 2
    for datas in produtos:
        datas = datas.datas



MargeSort()
