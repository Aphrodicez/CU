#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, m, start;
    cin >> n >> m >> start;
    vector <int> qs(100000 + 1);
    qs[0] = start;
    for(int i = 1; i <= n; i++) {
        int a, s;
        cin >> a >> s;
        qs[a] = s;
    }
    for(int i = 1; i <= 100000; i++) {
        if(qs[i] != 0) {
            start = qs[i];
        }
        qs[i] = qs[i - 1] + start;
    }
    for(int i = 1; i <= m; i++) {
        int p, x;
        cin >> p >> x;
        int lb = lower_bound(qs.begin(), qs.begin() + x + 1, p) - qs.begin();

        if(lb > x) {
            lb = lower_bound(qs.begin() + x + 1, qs.end(), p + qs[x]) - qs.begin();
        }
        cout << lb << ' ';
    }
    return 0;
}

/*
2 7 3
4 2
6 5
1 1000
3 1000
4 1000
12 1000
13 1000
14 1000
15 1000
*/