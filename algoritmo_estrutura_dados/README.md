# Primeiro Projeto(Algoritmo de Ordenação) 
    - Criar uma 1000 Produtos, contendo atributos como (Data,Valor,Avalização e Categoria)
    - Utilizar 4 algoritmos de ordenação para fazer isso(Bubble Sort, Quick Sort, Merge Sort, Heap Sort) 
    - Vou utilizar cada um desse algoritmo para ordenar determinado atributo 
    - Preço(Bubble Sort), Avaliação(Quick Sort), Data(Merge Sort), Categoria(Heap Sort)


Bubble Sort -> Analise o item com os seus adjacente para ver se é maior ou não assim substituindo-o 
    Se uma lista tiver 100 itens o item1 no pior dos casos ele passará por todos os itens e assim com o segundo até terminar 

Quick Sort -> Dividir para conquistar ele escolhe um elemento como pivo, e divide a lista em duas parte uma maior que o pivo e outra menor e então é chamdo 
recursivamente o processo para as sub-lista resultantes 

Merge Sort -> Dividir a lista até ela ficar só com os elementos separados, Depois comparar esse elementos para ver qual é maior e colocar eles em ordem em uma nova lista 
Com as novas lista formadas vamos pegar cada elemento dessas listas e compara-lós e colocando em uma nova lista 
    [9,7,3,1] -> Lista original 
    [9,7] [3,1] -> Separou pela metada 
    9, 7 , 3, 1 -> Dividiu a lista até os elementos ficarem unicos 
    [7,9] [1,3] -> Voltou as duas lista mas agora ordenadas 
    [1,3,7,9] -> juntou as duas lista de forma ordenada 

Heap Sort -> Uma árvore binaria quase completa organizada de maneira expecífica, sendo cada nó maior ou igual ao valor de seus filhos, fazando assim o maior elemento esta sempre na raiz
    O maior elemento (que esta na raiz do Max_Heap) é trocado com o último elemento do heap não ordenado 
    O tamanho do heap é reduzido em 1 (o ultimo elemnto trocado está agora em sua posição final ordenada) 
    O novo elemento raiz é empurrado para baixo (processo chamado de Heapify para restaurar a propriedade de Max_Heap na subestrutura restante 
    Esse processo se repete até que o tamanho de heap seja 1

# https://colab.research.google.com/drive/10R3EV77L3aG2rUE-kHNAjbWQzgolJsDe?usp=sharing
