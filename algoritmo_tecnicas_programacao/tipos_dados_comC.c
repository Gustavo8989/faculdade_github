#include <stdio.h> 
#include <math.h> 
#include <string.h> 

int main(){
    float nota1, nota2, media;
    printf("Digite as notas\n");
    scanf("%f",&nota1);
    scanf("%f",&nota2);
    media = (nota1 + nota2) / 2;
    printf("A Média do aluno é %.2f\n",media);
    printf("Fim do programa\n");
    
    return 0;
}
