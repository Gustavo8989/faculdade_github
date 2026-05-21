# Fita infinita -> Local do armazenamento de dados
# Cabeçote -> Lê e escreve na fita 
# Estados -> Controlam o comportamento
# Função de transição -> define as regas, nesse caso que leia L = {anbn | n>=0}

class MaquinaTuring:
    def __init__(self,fita,transicao,estado_inicial,estado_final):
        self.fita = list(fita) + ['_']
        self.inicio = 0
        self.trasicao = transicao
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final

    def etapa(self):
        simbolo = self.fita[self.inicio]
        if (self.estado_inicial, simbolo) not in self.trasicao:
            return False
        novo_simbolo,move,novo_estado = self.trasicao[(self.estado_inicial,simbolo)]
        self.fita[self.inicio] = novo_simbolo
        self.estado_inicial = novo_estado 
        if move == 'R':
            self.inicio += 1
            if self.inicio == len(self.fita):
                self.fita.append('_')
        elif move == 'L':
            self.inicio -= 1 
            if self.inicio < 0:
                self.fita.insert(0,'-')
                self.inicio = 0
        return True
    
    def run(self):
        while self.estado_inicial not in self.estado_final:
            if not self.etapa():
                print("Rejeitar")
                return
            print("Aceitar")

transquicao = {
    # Marca 'a'
    ('q0', 'a'): ('X', 'R', 'q1'),
    ('q0', 'X'): ('X', 'R', 'q0'),
    ('q0', 'Y'): ('Y', 'R', 'q3'),

    # Procura 'b'
    ('q1', 'a'): ('a', 'R', 'q1'),
    ('q1', 'Y'): ('Y', 'R', 'q1'),
    ('q1', 'b'): ('Y', 'L', 'q2'),

    # Volta
    ('q2', 'a'): ('a', 'L', 'q2'),
    ('q2', 'X'): ('X', 'L', 'q2'),
    ('q2', 'Y'): ('Y', 'L', 'q2'),
    ('q2', '_'): ('_', 'R', 'q0'),

    # Verifica final
    ('q3', 'Y'): ('Y', 'R', 'q3'),
    ('q3', '_'): ('_', 'R', 'qf')
}

maquina = MaquinaTuring(
    fita="aabb",
    transicao=transquicao,
    estado_inicial='q0',
    estado_final={'qf'}
)

maquina.run()