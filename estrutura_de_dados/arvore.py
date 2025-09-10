class Node:
    def __init__(self,valor,direita:None,esquerda:None):
        self.valor = valor
        self.direita = None 
        self.esquerda = None
    def verificando(self):

root = Node(5)
root.direita = Node(6)
root.esquerda = Node(3)
