#include <bits/stdc++.h>
using namespace std;


int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, m, k;
    cin >> n >> m >> k;
    vector <int> vec(n);
    for(int i = 0; i < n; i++) {
        cin >> vec[i];
    }
    sort(vec.begin(), vec.end());
    for(int i = 1; i <= m; i++) {
        int p;
        cin >> p;
        cout << upper_bound(vec.begin(), vec.end(), p + k) - lower_bound(vec.begin(), vec.end(), p - k) << ' ';
    }
    return 0;
}

/*
5 5 1
1 3 5 9 10
1 2 3 7 20
*/