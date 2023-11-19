#include <bits/stdc++.h>
using namespace std;

map <int, int> mp;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        int val;
        cin >> val;
        mp[val] = 1;
        if(val < 1 || val > n) {
            cout << "NO\n";
            return 0;
        }
    }
    cout << ((int)mp.size() == n ? "YES" : "NO") << '\n';
    return 0;
}

/*
4
4 1 3 2

7
-1 -2 3 0 2 3 4

5
5 4 3 1 3
*/