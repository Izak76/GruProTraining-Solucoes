/* 
OBS: Este algoritmo está escrito em C++ porquê a versão em Python
(de onde este algoritmo foi "traduzido") estava dando problema de
"Tempo limite excedido".

Para ver a versão em Python, acesse: https://bit.ly/3DjtzDH
*/

#include <iostream>
#include <cmath>
using namespace std;
typedef unsigned long ul;

int main() {
    int x=0, y=0, d;
    ul n, m;
    short ex = 0;
    char c;
    cin >> n >> m;
    
    for (ul i=0; i<n; i++){
        cin >> c >> d;
        switch (c){
            case 'N':
                y += d;
                break;
            case 'S':
                y -= d;
                break;
            case 'L':
                x += d;
                break;
            case 'O':
                x -= d;
                break;
        }

        if (hypot(x, y) > m){
            ex = 1;
            break;
        }
    }
    cout << ex << endl;
}