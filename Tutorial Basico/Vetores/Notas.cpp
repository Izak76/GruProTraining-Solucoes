#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

bool comp(pair<short, short> x, pair<short, short> y){
    if (x.second == y.second){
        return x.first < y.first;
    }

    return x.second < y.second;
}

int main(){
    short  n, nt;
    cin >> n;

    map<short, short> notas;
    for(short i=0; i<n; i++){
        cin >> nt;
        notas.emplace(nt, 0);
        notas[nt]++;
    }

    cout << (*max_element(notas.begin(), notas.end(), comp)).first << endl;
}
