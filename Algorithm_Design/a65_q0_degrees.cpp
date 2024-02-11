#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n;
    cin >> n;
    vector <vector <int>> a(n, vector <int> (n));
    vector <int> deg(n, 0);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> a[i][j];
            if(a[i][j]) {
                deg[j]++;
            }
        }
    }
    vector <int> cnt(n, 0);
    int k = 0;
    for(int i = 0; i < n; i++) {
        cnt[deg[i]]++;
        k = max(k, deg[i]);
    }
    for(int i = 0; i <= k; i++) {
        cout << cnt[i] << " ";
    }
    return 0;
}

/*
6 
0 1 0 1 0 0 
1 0 1 0 0 0 
0 1 0 0 0 0 
1 0 0 0 1 1 
0 0 0 1 0 1 
0 0 0 1 1 0 
*/