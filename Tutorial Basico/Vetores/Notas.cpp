//Este algoritmo � uma "tradu��o" da vers�o em python. Ela est� dispon�vel em: 
/*Por mais estranho que pare�a, mesmo que ambas as vers�es (Python e C++)
funcionem praticamente da mesma forma, somente a vers�o em C++ (esta aqui)
� aceita no sistema de corre��o. A vers�o em Python d� "Resposta errada".
Por qual motivo? Bom, eu n�o sei e n�o entendo o por qu�.*/

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
    short maior=0, cmaior=0, ct; //O maior n�mero e a quantidade dele no array, respectivamente
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
