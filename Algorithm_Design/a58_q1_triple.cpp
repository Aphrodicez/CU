#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, m;
    cin >> n >> m;
    vector <int> a(n);
    map <int, vector <pair <int, int>>> mp;
    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            mp[a[i] + a[j]].emplace_back(make_pair(i, j));
        }
    }
    while(m--) {
        int sum;
        cin >> sum;
        bool ch = false;
        for(int i = 0; i < n; i++) {
            for(auto &p : mp[sum - a[i]]) {
                if(i != p.first && i != p.second) {
                    ch = true;
                    break;
                }
            }
            if(ch) {
                break;
            }
        }
        if(ch) {
            cout << "YES\n";
        }
        else {
            cout << "NO\n";
        }
    }
    return 0;
}

/*
4 5
-2 1 5 6
1 3 5 6 7
*/