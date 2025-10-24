# Primeiro Projeto(Algoritmo de Ordenação) 
    - Criar uma 1000 Produtos, contendo atributos como (Data,Valor,Avalização e Categoria)
    - Utilizar 4 algoritmos de ordenação para fazer isso(Bubble Sort, Quick Sort, Merge Sort, Heap Sort) 
    - Vou utilizar cada um desse algoritmo para ordenar determinado atributo 
    - Preço(Bubble Sort), Avaliação(Quick Sort), Data(Merge Sort), Categoria(Heap Sort)


Bubble Sort -> Analise o item com os seus adjacente para ver se é maior ou não assim substituindo-o 
    Se uma lista tiver 100 itens o item1 no pior dos casos ele passará por todos os itens e assim com o segundo até terminar 

Quick Sort -> Dividir para conquistar ele escolhe um elemento como pivo, e divide a lista em duas parte uma maior que o pivo e outra menor 

Merge Sort -> Dividir a lista até ela ficar só com os elementos separados, Depois comparar esse elementos para ver qual é maior e colocar eles em ordem em uma nova lista 
    com as novas lista formadas vamos pegar cada elemento dessas listas e compara-lós e colocando em uma nova lista 
    [9,7,3,1] 
    [9,7] [3,1]
    9, 7 , 3, 1
    [7,9] [1,3]
    [1,3,7,9]
    