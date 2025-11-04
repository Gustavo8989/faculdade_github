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
                 produtos[k], produtos[k+1] = produtos[k+1],produtos[k]

# Avaliação
def QuickSort():
    pivo = int(len(produtos)) // 2
    maior = []
    menor = []
    result = []
    for c in range(n):
        if pivo > c:
            menor.append(c)
        elif pivo < c:
            maior.append(c)
    # Modificar a lista produtos 
        result = menor + maior
        produtos[c][1] = result


# Data
def MargeSort(key=lambda x:x):
    # Separar a lista em varias partes menores até ficar com os valores unicos 
    meio = n // 2
    esquerda = MargeSort(produtos[:meio])
    direita = MargeSort(produtos[meio:])
    #Mesclando 
    resultado =[]
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if key(esquerda[i] <= key(direita[i])):
            resultado.append(esquerda[i])
            i += 1 
        else:
            resultado.append(direita[i])
            j += 1 

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:]) 
    return resultado 



# Categoria 
lista = produtos
def HeapSort():
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    if esquerda < n and key(lista[esquerda]) > key(lista[maior]):
        maior = esquerda
    if direita < n and key(lista[direita]) > key(lista[maior]):
        maior = direita
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior, key)


def heap_sort(lista, key=lambda x: x):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i, key)
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i] 
        heapify(lista, i, 0, key)
    return lista

print(produtos[1])
