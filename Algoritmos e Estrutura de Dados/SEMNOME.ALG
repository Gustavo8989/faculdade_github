Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor   : Antonio Carlos Nicolodi 

var
   time_A : inteiro
   time_B : inteiro
   difereca : inteiro
Inicio
      escreva("Digite o n�mero de gols do time A: ")
      Leia(time_A)
      escreva("DIgite o n�mero de gols do time B: ")
      Leia(time_b)
      difereca <- time_A - time_B
      escreva(" A diferen�a do Time A para O Time B foi de",difereca)
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