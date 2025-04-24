#include <iostream>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	double waat,waat_menor,waat_maior;
	int quantidade = 0;
	cout << "Bem Vindo ao programa" << endl;
	cout << "Nesse programa mostraremos o maior valor de Watt no dia" << endl;
	while(quantidade<20){
		cin >> waat;
		if (quantidade == 0){
			waat_maior = waat;
			waat_menor = waat_maior;
		}else if(waat > waat_maior){
			waat_maior = waat;
		}else if(waat < waat_menor){
			waat_menor = waat;
		}
		quantidade++;
		
		}
		cout << "O Maior valor foi de " << waat_maior << endl;
	}
