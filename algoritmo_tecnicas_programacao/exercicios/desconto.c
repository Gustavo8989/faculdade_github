#include <stdio.h> 

int main(){
    int tipo_produto = 2;
    float preco = 100.00;
    float desconto;
    switch (tipo_produto){
        case 1:
            desconto = preco * 0.1;
            break;
        case 2:
            desconto = preco * 0.2;
            break;
        case 3:
            desconto = preco * 0.3;
            break;
        case 4:
            desconto = preco * 0.4;
            break;
        default = 0;
        }
    float precoComDesconto = preco - desconto;
    printf("O preço com desconto vai ser de %.2f",precoComDesconto);
}


