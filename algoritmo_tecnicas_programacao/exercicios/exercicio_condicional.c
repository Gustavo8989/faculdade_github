/*
1-) Controle de combustível: se o nível de combustível estiver abaixo de 20%, exiba uma mensagem de alerta.
2-) Orientação da nave: se a nave estiver fora da rota programada, corrija automaticamente a trajetória.
3-) Condições climáticas: se for identificada uma tempestade solar, ative o protocolo de proteção da nave
*/
#include <stdio.h> 

int main(){
    double nivel_conbus;
    printf("Digite o numero de combustivel da nave \n");
    scanf("%d",&nivel_conbus);
    if (nivel_conbus < 100.00){
        printf("Combustivel baixo \n");
    }
    else if (nivel_conbus < 50.00){
        printf("Combustivel muito baixo \n");
    }
    else if (nivel_conbus <= 0){
        printf("Sem combustivel \n");
    }
    else{
        printf("Nivel de combustivel alto \n");
    }
    float orientacao_nave;
    printf("Informe quantos graus a nave está \n");
    scanf("%f",&orientacao_nave);
    if (orientacao_nave > 45.5){
        printf("esta fora de orbita \n");
    }
    else{
        printf("Está dentro da orbita \n");
    }
    int tempestade_solar;
    printf("Esta mercado uma tempestade solar? \n");
    scanf("%d",&tempestade_solar);
    if (tempestade_solar == 1){
        printf("Sim esá mercado \n");
    }
    else{
        printf("Não esta mercando \n");
    }
}    



