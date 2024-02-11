#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 20;

int ans[MAX_N];

int n, k;

void recur(int state, int consec, int max_consec) {
    if(state == n) {
        if(max_consec < k) {
            return ;
        }
        for(int i = 0; i < n; i++) {
            cout << ans[i];
        }
        cout << '\n';
        return ;
    }
    ans[state] = 0;
    recur(state + 1, 0, max_consec);
    ans[state] = 1;
    recur(state + 1, consec + 1, max(max_consec, consec + 1));
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    cin >> n >> k;
    recur(0, 0, 0);
    return 0;
}

/*
5 3
*/