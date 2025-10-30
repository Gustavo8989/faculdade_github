''' 
Atividade Proposta:
Você trabalha em uma empresa de tecnologia que está desenvolvendo um sistema de
gerenciamento de dados. Para otimizar as operações de busca, inserção e remoção, você foi
designado para implementar uma Árvore AVL que manterá os dados balanceados.
'''

class Node(object):
    def __init__(self,key,value=None,left=None,right=None):
        self.key = key
        self.value = value
        self.left = left 
        self.right = right


class AVL:

    def altura(self,Node):
        if Node is None:
            return 0
        else:
            return Node.altura

    def balanceamento(self,Node):
        if Node is None:
            return 0
        else:
            return self.altura(Node.left) - self.altura(no.right)

    def rotacao_direita(self,Node):
        pass 

    def rotacao_esquerda(self,Node):
        pass 


    def insercao(self,val,raiz):
        if raiz is None:
            return no(val)
