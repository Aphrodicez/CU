#include <bits/stdc++.h>
using namespace std;

vector <int> qs;

bool divide(int l, int r) {
    int sz = r - l + 1;
    if(sz < 4) {
        return true;
    }
    int mid = (l + r) / 2;
    return abs((qs[r] - qs[mid]) - (qs[mid] - qs[l - 1])) <= 1 && divide(l, mid) && divide(mid + 1, r);
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, k;
    cin >> n >> k;
    int sz = 1;
    for(int i = 0; i < k; i++) {
        sz *= 2;
    }
    qs.resize(sz + 1, 0);
    while(n--) {
        for(int i = 1; i <= sz; i++) {
            cin >> qs[i];
            qs[i] += qs[i - 1];
        }
        if(divide(1, sz)) {
            cout << "yes\n";
        }
        else {
            cout << "no\n";
        }
    }
    return 0;
}

/*
5 2 
0 0 0 0 
0 0 1 1  
0 1 1 1 
1 0 0 0 
0 1 0 1
*/