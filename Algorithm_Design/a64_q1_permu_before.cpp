#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 20;

vector <int> pre[MAX_N];

int pos[MAX_N];

int ans[MAX_N];

int n, m;

void recur(int state) {
    if(state == n) {
        for(int i = 0; i < n; i++) {
            cout << ans[i] << " ";
        }
        cout << '\n';
        return ;
    }
    for(int i = 0; i < n; i++) {
        if(pos[i]) {
            continue;
        }
        bool ch = true;
        for(int &x : pre[i]) {
            if(!pos[x]) {
                ch = false;
            }
        }
        if(!ch) {
            continue;
        }
        pos[i] = state + 1; // [1, n]
        ans[state] = i;
        recur(state + 1);
        pos[i] = 0;
        ans[state] = 0;
    }
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    cin >> n >> m;
    for(int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        pre[b].emplace_back(a);
    }
    recur(0);
    return 0;
}

/*
4 2 
3 2 
2 1
*/