#include <bits/stdc++.h>
using namespace std;

map <long long, long long> parent;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, m;
    cin >> n >> m;
    for(int i = 1; i <= n; i++) {
        long long f, s;
        cin >> f >> s;
        parent[s] = f;
    }
    for(int i = 1; i <= m; i++) {
        long long a, b;
        cin >> a >> b;
        long long ga = parent[parent[a]];
        long long gb = parent[parent[b]];
        if(a == b || ga == 0ll || gb == 0ll || ga != gb) {
            cout << "NO" << '\n';
        }
        else {
            cout << "YES" << '\n';
        }
    }
    return 0;
}

/*
5 4
1 2
1 3
2 20
3 30
2 21
1 2
2 30
30 20
20 20

3 2
1110001110001 1110001110002
1110001110001 1110001110003
1110001110003 1110001110009
1334 22
18273625162 283
*/