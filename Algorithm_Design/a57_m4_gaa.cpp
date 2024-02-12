#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n;
    cin >> n;
    vector <int> g(100010);
    g[0] = 3;
    int i;
    for(i = 1; ; i++) {
        g[i] = g[i - 1] + (i + 3) + g[i - 1];
        if(g[i] > 1000000000) {
            break;
        }
    }
    if(g[i] == 0) {
        i--;
    }
    while(true) {
        if(i == 0) {
            if(n == 1) {
                cout << "g";
            }
            else {
                cout << "a";
            }
            break;
        }
        else if(n <= g[i - 1]) {
            i--;
        }
        else if(n <= g[i - 1] + (i + 3)) {
            if(n == g[i - 1] + 1) {
                cout << "g";
            }
            else {
                cout << "a";
            }
            break;
        }
        else {
            n -= g[i - 1] + (i + 3);
            i--;
        }
    }
    return 0;
}

/*

*/