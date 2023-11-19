#include <bits/stdc++.h>
using namespace std;

map <string, int> mp;
vector <int> vec;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, k;
    cin >> n >> k;
    for(int i = 1; i <= n; i++) {
        string s;
        cin >> s;
        mp[s]++;
    }
    for(map <string, int> :: iterator it = mp.begin(); it != mp.end(); it++) {
        vec.emplace_back(it->second);
    }
    sort(vec.begin(), vec.end(), greater <int>());
    cout << vec[min((int)vec.size() - 1, k - 1)];
    return 0;
}

/*
8 2
somchai
adisak
somchai
yingyos
somchai
adisak
direk
yingyos

5 3
somchai
somchai
somchai
somchai
yingyos
*/