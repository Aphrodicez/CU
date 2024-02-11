#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 20;

int ans[MAX_N];

int b;

void recur(int state, int k) {
    if(state == b) {
        if(k) {
            return ;
        }
        for(int i = 0; i < b; i++) {
            cout << ans[i];
        }
        cout << '\n';
        return ;
    }
    ans[state] = 0;
    recur(state + 1, k);
    ans[state] = 1;
    recur(state + 1, k - 1);
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int a;
    cin >> a >> b;
    recur(0, a);
    return 0;
}

/*
2 5
*/