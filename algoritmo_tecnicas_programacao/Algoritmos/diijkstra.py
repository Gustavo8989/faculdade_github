'''
Em um cenário urbano em constante evolução, considere uma rede de transporte inteligente (ITS) que monitora o tráfego em tempo real, acidentes
,obras e eventos especiais. O objetivo é fornecer aos motoristas a rota mais rápida do ponto A ao ponto B, considerando que os pesos das 
arestas (tempos de viagem) mudam constantemente devido às condições do tráfego.
'''
import random

def trafego():
    vertises = ['A', 'B', 'C', 'D', 'E', 'F']
    grafo = {}
    grafo["A"] = {}
    grafo["B"] = {}
    grafo["C"] = {}
    grafo["D"] = {}
    grafo["E"] = {}
    
    grafo["A"]["B"] = 2
    grafo["A"]["C"] = 3
    grafo["B"]["D"] = 8 
    grafo["D"]["F"] = 7
    grafo["C"]["E"] = 9
    grafo["E"]["F"] = 4 
    print(grafo)
    
    contra_tempo = {random.choice(vertises):random.randint(20,40)} # Definindo o contra-tempo com valores

trafego()
