#include <bits/stdc++.h>
using namespace std;

vector <int> v;

bool divide(int l, int r) {
    if(r - l + 1 == 2) {
        if(v[l] == 0 && v[r] == 1) {
            return true;
        }
        else {
            return false;
        }
    }
    int mid = (l + r) / 2;
    if(!divide(mid + 1, r)) {
        return false;
    }
    if(divide(l, mid)) {
        return true;
    }
    reverse(v.begin() + l, (v.begin() + mid) + 1);
    bool res = divide(l, mid);
    reverse(v.begin() + l, (v.begin() + mid) + 1);
    return res;
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, k;
    cin >> n >> k;
    int sz = 1;
    for(int i = 0; i < k; i++) {
        sz *= 2;
    }
    v.resize(sz);
    while(n--) {
        for(int i = 0; i < sz; i++) {
            cin >> v[i];
        }
        if(divide(0, sz - 1)) {
            cout << "yes\n";
        }
        else {
            cout << "no\n";
        }
    }
    return 0;
}

/*
4 1 
0 1 
1 0 
0 0 
1 1

3 3
1 0 0 1 0 1 0 1 
1 0 1 0 1 0 0 1 
1 0 1 1 1 0 0 0
*/