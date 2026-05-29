#include <iostream>
#include <omp.h>
#include <cstdlib>
#include <ctime>

using namespace std;

#define N 3

int main(){
    int matriz1[N][N];
    int matriz2[N][N];
    int resultado[N][N];

    for (int i=0;int<N;i++){
        for(int j=0;j<N;j++){
            matriz1[i][j] = rand() % 10;
            matriz2[i][j] = rand() % 10;

        }
    }
    for (int i = 0; i < N; i++){
        for(int j=0; j < N; j++){
            int resultado[i][j] = 0;
            for(int k=0; k < N; k++){
                int resultado = matriz1[i][k] * matriz2[k][j];
            }
        }      
    }
    cout << "Matriz 1" << endl;
    for(int c=0;c<N;c++){
        for(int t=0;t<N;t++){
            cout << matriz1[c][t] << endl;
        }
    }
    cout << "Matriz 2" << endl;
    for(int c=0;c<N;c++){
        for(int t=0;t<N;t++){
            cout << matriz2[c][t] << endl;
        }
    }
    for(int c=0;c<N;c++){
        for(int t=0;t<N;t++){
            cout << resultado[c][t] << endl;
        }
    }
    return 0;
}