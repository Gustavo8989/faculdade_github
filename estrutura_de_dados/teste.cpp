#include <iostream>
using namespace std;

void Ordena(Produtos* l){
    Produtos* prod; 
    Produtos* aux;
    int temp;
    for (prod = l; prod != NULL; prod = prod -> prox){
        for(aux = prod -> prox; aux != NULL; aux = aux -> prox){
            if ((prod -> info) > (aux -> info)){
                temp = prod -> info;
                prod -> info = aux -> info;
                aux -> info = temp; 
            }
        }
    }
}

