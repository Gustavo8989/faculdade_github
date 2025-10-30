import random 

class Graph:
    # grafo [A:2]
    def __init__(self,indice,valor):
        self.indice = indice 
        self.valor = valor 

    def __repr__(self):
        return f"{self.indice}: {self.valor}"




def gerando_grafo():
    grafo = []
    indice = ["A","B","C","D"]
    final = "E"
    valores = [round(random.uniform(0,20)) for c in range(len(indice))]
    grafo = [Graph(indice[c],valores[c]) for c in range(len(indice))]
    caminhos = [grafo for c in range(5)]
    return caminhos


grafo = gerando_grafo()

def visualizando_grafo():
    for t in grafo:
        print(t)

def dikstraj():
    pass 

visualizando_grafo()

















