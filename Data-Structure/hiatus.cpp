#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, m;
    cin >> n >> m;
    vector <pair <int, int>> vec(n);
    for(int i = 0; i < n; i++) {
        cin >> vec[i].first >> vec[i].second;
    }
    sort(vec.begin(), vec.end());
    for(int i = 1; i <= m; i++) {
        int year, month;
        cin >> year >> month;
        int idx = upper_bound(vec.begin(), vec.end(), make_pair(year, month)) - vec.begin() - 1;
        if(idx == -1) {
            cout << -1 << ' ' << -1 << ' ';
        }
        else if(vec[idx] == make_pair(year, month)) {
            cout << 0 << ' ' << 0 << ' ';
        }
        else {
            cout << vec[idx].first << ' ' << vec[idx].second << ' ';
        }
    }
    return 0;
}

/*
3 4
2019 10
2020 1
2020 8
2020 1
2019 12
2020 11
2018 1

2 3
100000 1
1 12
1 12
1 11
100000 2
*/