//Este algoritmo é uma "tradução" da versão em python. Ela está disponível em: 
/*Por mais estranho que pareça, mesmo que ambas as versões (Python e C++)
funcionem praticamente da mesma forma, somente a versão em C++ (esta aqui)
é aceita no sistema de correção. A versão em Python dá "Resposta errada".
Por qual motivo? Bom, eu não sei e não entendo o por quê.*/

#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    short nn;
    cin >> nn;
    short n[nn];
    for(short x=0; x<nn; x++){
        cin >> n[x];
    }
    short maior=0, cmaior=0, ct; //O maior número e a quantidade dele no array, respectivamente
    for (short x: n){
        ct = count(n, n+nn, x);
        if (ct > cmaior){
            maior = x;
            cmaior = ct;
        }
        else if (ct == cmaior && x > maior){
            maior = x;
        }
    }
    cout << maior << endl;
}
