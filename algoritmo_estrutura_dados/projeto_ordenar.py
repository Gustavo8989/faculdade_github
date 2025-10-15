from datetime import datetime
import random 


class Produto:
    def __init__(self,produto:str,preco:int,avaliacao:float,data_adicao:datetime,categoria:str):       
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
    categoria = ["Categoria: " + str(random.radint(0,5)) for c in range(n)]
    produto = [Produto(nome[i], preco[i], avaliacao[i],datas[i],categoria[i]) for i in range(n)]
    return produto



produtos = gerando_dados(1000)
for produto in produtos[:10:]:
    print(produto)