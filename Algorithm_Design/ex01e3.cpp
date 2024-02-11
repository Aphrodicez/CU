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
        auto it = upper_bound(v.begin(), v.end(), x);
        if(it == v.begin()) {
            cout << -1 << '\n';
        }
        else {
            cout << *(it - 1) << '\n';
        }
    }
    return 0;
}

/*
4 7
14 15 20 30
10 11 14 15 16 21 68
*/