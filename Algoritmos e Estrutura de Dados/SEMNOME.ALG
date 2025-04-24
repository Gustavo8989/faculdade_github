Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 

var
   time_A : inteiro
   time_B : inteiro
   difereca : inteiro
Inicio
      escreva("Digite o número de gols do time A: ")
      Leia(time_A)
      escreva("DIgite o número de gols do time B: ")
      Leia(time_b)
      difereca <- time_A - time_B
      escreva(" A diferença do Time A para O Time B foi de",difereca)
      se time_A > time_B entao
         escreva("Time A venceu")
      senao
         se time_B > time_A entao
            escreva("Time B venceu")
         senao
              escreva("Empate")
         fimse
fimse

Fimalgoritmo