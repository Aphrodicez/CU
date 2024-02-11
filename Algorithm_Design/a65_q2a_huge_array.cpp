#include <bits/stdc++.h>
using namespace std;


int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, q;
    cin >> n >> q;
    vector <pair <int, int>> qs(n + 1);
    qs[0] = make_pair(0, 0);
    for(int i = 1; i <= n; i++) {
        cin >> qs[i].first >> qs[i].second;
    }
    sort(qs.begin(), qs.end());
    for(int i = 1; i < (int)qs.size(); i++) {
        qs[i].second += qs[i - 1].second;
    }
    while(q--) {
        int p;
        cin >> p;
        int l = 1, r = qs.size();
        while(l < r) {
            int mid = (l + r) / 2;
            if(qs[mid].second < p) {
                l = mid + 1;
            }
            else {
                r = mid;
            }
        }
        cout << qs[l].first << '\n';
    }
    return 0;
}

/*
5 2 
1 1 
10 1 
5 1 
1 1 
3 1 
5 
1

5 3 
9 1 
4 5 
9 3 
8 3 
7 7 
1 
15 
8 
*/