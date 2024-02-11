#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 8;

int p[MAX_N], h[MAX_N];
int t[MAX_N];

int ans = 0;

int n, m, k, w;

void recur(int state) {
    if(state == k) {
        int sum = 0;
        for(int i = 0; i < m; i++) {
            sum += h[i];
        }
        ans = min(ans, sum);
        return ;
    }
    for(int i = 0; i < m; i++) {
        bool canShoot = h[i] > 0 && t[state] - w <= p[i] && p[i] <= t[state] + w;
        if(canShoot) {
            h[i]--;
        }
        recur(state + 1);
        if(canShoot) {
            h[i]++;
        }
    }
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    cin >> n >> m >> k >> w;
    for(int i = 0; i < m; i++) {
        cin >> p[i];
    }
    for(int i = 0; i < m; i++) {
        cin >> h[i];
        ans += h[i];
    }
    for(int i = 0; i < k; i++) {
        cin >> t[i];
    }
    recur(0);
    cout << ans << '\n';
    return 0;
}

/*
10 1 2 1
1
10
2 5

10 1 2 4 
1 
10 
2 5

100 3 3 1 
80 70 60 
1 1 1 
70 71 69 
*/