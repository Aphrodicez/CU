#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, m;
    cin >> n >> m;
    vector <int> v(n);
    for(int i = 0; i < n; i++) {
        cin >> v[i];
    }
    while(m--) {
        int x;
        cin >> x;
        cout << (upper_bound(v.begin(), v.end(), x) - v.begin()) - 1 << '\n';
    }
    return 0;
}

/*
10 8
10 13 14 14 14 15 16 16 18 200
9 10 11 14 0 200 20 16
*/