#include <iostream>
#include <omp.h>
using namespace std;

int main(){
    int matriz1[3][3] = {
        1,2,3,
        4,5,6,
        7,8,9,
    };
    int matriz2[3][3]{
        2,4,6,
        1,3,5,
        8,9,4,
    };

    int matriz_soma[N][N];
    #pragma omp parallel for
    //Primeiro elementos[x1] da primeira matriz e multiplico pelo primeiro elementos da segunda matriz
    for (int i = 0; i < 3; i++){
        for(int j=0; j < 3; j++){
            int soma = matriz1[i][j] * matriz2[i][j];
            matriz_soma[i][j] = soma;
        }      
    }
    for(int c=0;c<3;c++){
        for(int t=0;t<3;t++){
            cout << matriz_soma[c][t] << endl;
        }
    }
    return 0;
}