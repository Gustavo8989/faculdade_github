import datetime
import random 


class Produto:
    def __init__(self,data_adicao:datetime.datetime,produto:str,preco:int,avaliacao:float,categoria:str):       
        self.produto = produto 
        self.preco = preco 
        self.avaliacao = avaliacao 
        self.data_adicao = data_adicao 
        self.categoria = categoria 

    def __repr__(self):
        return f"{self.produto}: {self.preco}, {self.avaliacao}, {self.data_adicao}, {self.categoria}"
   

def gerando_dados(n):
    nome = ["Produtos " + str(c) for c in range(n)]
    preco = [round(random.uniform(0,1000),2) for c in range(n)]
    avaliacao = [round(random.uniform(0,5),2) for _ in range(n)]
    datas = [datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365)) for _ in range(n)]
    categoria = ["Categoria: " + str(random.randint(0,5)) for c in range(n)]
    produto = [Produto(datas[i],nome[i], preco[i], avaliacao[i],categoria[i]) for i in range(n)]
    return produto

produtos = gerando_dados(1000)

def visualizar():
    for produto in produtos:
        print(produto)

def buble_sort():
    n = len(produtos)
    for c in range(n):
        # Esta percorendo a lista inteira proporcional a quantidade de itens, Nesse caso a lista vai se repetir 1000 vezes 
        for k in range(0, n-c-1):
            # Verificando se o numero é maior ou menos
            if produtos[k].preco > produtos[k+1].preco:
                # Trocando de lugar
                pass 

def QuickSort():
    pass 
