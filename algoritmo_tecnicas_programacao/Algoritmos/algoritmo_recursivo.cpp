#include <iostream> 

using namespace std;

int main(){
    return 0;
}

int Fato(int n){
    int n;
    cin >> n;
    if (n==0){
        return 1;
    }else{
        return n * Fato(n-1);
    }
}
